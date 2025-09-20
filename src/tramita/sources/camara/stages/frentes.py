# tramita/sources/camara/stages/frentes.py

from typing import Iterable

import logging


from tramita.config import settings
from tramita.http.client import HttpClient
from tramita.log import setup_logging
from tramita.sources.base import bounded_gather_pbar
from tramita.sources.camara.client import camara_fetch
from tramita.storage.manifest import SnapshotManifest
from tramita.storage.parquet import write_details_parts, write_relation_parts
from tramita.storage.paths import BronzePaths
from tramita.sources.camara.utils.bucketing import _bucket_year_for_items
from tramita.sources.camara.utils.extractors import (
    _extract_author_targets,
    _extract_frente_ids,
    _extract_relatores_from_tramitacoes,
)

log = logging.getLogger(__name__)


CAMARA_BASE = settings.camara_base_url.rstrip("/")


async def build_frentes_via_deputados(
    paths: BronzePaths,
    manifest: SnapshotManifest,
    years: Iterable[int],
    *,
    page_size: int = 100,
    concurrency_deputados: int = 16,
    concurrency_frentes: int = 16,
) -> tuple[int, int, int]:
    """
    1) Read camara/autores and camara/tramitacoes parts for the selected years,
       parse payload_json and collect relevant deputado IDs (+ first-seen year).
    2) For each deputado -> GET /deputados/{id}/frentes, write relation 'deputados/frentes'
       bucketed by first date seen in payload (fallback: earliest selected year).
       Collect frente IDs + first-seen year.
    3) Fetch /frentes/{fid} (details, year=0000) and /frentes/{fid}/membros
       (relation bucketed by first date in payload).
    Returns (#dep_frentes_rows, #frentes_details, #frentes_membros_rows).
    """
    import json
    import pyarrow.parquet as pq

    setup_logging()
    y0 = min(years) if years else 0
    default_bucket = y0

    first_seen_dep: dict[str, int] = {}

    # --- 1) read autores + tramitacoes parts to find deputados ---
    for y in years:
        for rel in ("autores", "tramitacoes"):
            d = paths.relation_part_dir("camara", rel, y)
            if not d.exists():
                continue
            for part in sorted(d.glob("part-*.parquet")):
                t = pq.read_table(part, columns=["payload_json"])
                for r in t.to_pylist():
                    try:
                        obj = json.loads(r["payload_json"])
                        dados = obj.get("dados") or []
                    except Exception:
                        continue
                    if rel == "autores":
                        deps, _ = _extract_author_targets(dados)
                    else:
                        deps = _extract_relatores_from_tramitacoes(dados)
                    for dep in deps:
                        first_seen_dep.setdefault(dep, y)

    dep_ids = sorted(first_seen_dep.keys(), key=int) if first_seen_dep else []
    if not dep_ids:
        log.info("[camara:frentes] no relevant deputados found; skipping")
        return (0, 0, 0)

    first_seen_frente: dict[str, int] = {}

    async with HttpClient(
        CAMARA_BASE, rate_per_sec=settings.camara_rate,
        timeout=settings.http_timeout, user_agent=settings.user_agent
    ) as hc:
        async def dep_worker(dep_id: str):
            dados = await camara_fetch(
                hc, f"/deputados/{dep_id}/frentes", {},
                itens=page_size,
            )
            y = _bucket_year_for_items(dados, years, first_seen_dep.get(dep_id, default_bucket))
            row = {
                "source": "camara",
                "entity": "deputados/frentes",
                "year": y,
                "id": dep_id,
                "url": f"{CAMARA_BASE}/deputados/{dep_id}/frentes",
                "payload_json": json.dumps({"dados": dados}, ensure_ascii=False, separators=(",", ":"), sort_keys=True),
            }
            for fid in _extract_frente_ids(dados):
                first_seen_frente.setdefault(fid, y)
            return row

        dep_rows, dep_errs = await bounded_gather_pbar(
            dep_ids, dep_worker, concurrency=concurrency_deputados, description="camara:deputados_frentes",
        )
        if dep_errs:
            log.warning(f"[camara:deputados/frentes] errors={len(dep_errs)}")

    # write deputados/frentes grouped by year
    dep_count = 0
    for y in sorted({r["year"] for r in dep_rows}):
        rows_y = [r for r in dep_rows if r["year"] == y]
        parts = write_relation_parts(
            rows_y, paths=paths, manifest=manifest,
            source="camara", relation="deputados/frentes", year=int(y),
            part_rows=50_000, sort=True
        )
        dep_count += len(rows_y)
        log.info(f"[camara:deputados/frentes] year={y} wrote {len(rows_y)} rows in {len(parts)} part(s)")

    # --- 3) fetch frentes details + membros only for discovered IDs ---
    frentes_by_year: dict[int, list[str]] = {}
    for fid, y in first_seen_frente.items():
        frentes_by_year.setdefault(y, []).append(fid)

    fr_det_count = fr_mem_count = 0

    async with HttpClient(
        CAMARA_BASE, rate_per_sec=settings.camara_rate,
        timeout=settings.http_timeout, user_agent=settings.user_agent
    ) as hc:
        async def fr_det_worker(fid: str):
            url = f"/frentes/{fid}"
            dados = await camara_fetch(hc, url, None)
            return {
                "source": "camara",
                "entity": "frentes",
                "year": 0,
                "id": fid,
                "url": CAMARA_BASE + url,
                "payload_json": json.dumps(
                    {"dados": dados}, ensure_ascii=False, separators=(",", ":"), sort_keys=True
                ),
            }

        det_ids = sorted(first_seen_frente.keys(), key=int)
        det_rows, det_errs = await bounded_gather_pbar(
            det_ids, fr_det_worker, concurrency=concurrency_frentes, description="camara:deputados_frentes"
        )
        if det_errs:
            log.warning(f"[camara:frentes(details)] errors={len(det_errs)}")
        if det_rows:
            dp = write_details_parts(
                det_rows, paths=paths, manifest=manifest,
                source="camara", entity="frentes", year=0,
                part_rows=50_000, sort=True
            )
            fr_det_count = len(det_rows)
            log.info(f"[camara:frentes] wrote {len(det_rows)} details in {len(dp)} part(s) → year=0000")

        # membros (bucket by first date in list; fallback=first-seen year)
        async def fr_mem_worker(fid: str, yy: int):
            dados = await camara_fetch(
                hc, f"/frentes/{fid}/membros", {},
                itens=page_size,
            )
            y = _bucket_year_for_items(dados, years, yy)
            return {
                "source": "camara",
                "entity": "frentes/membros",
                "year": y,
                "id": fid,
                "url": f"{CAMARA_BASE}/frentes/{fid}/membros",
                "payload_json": json.dumps({"dados": dados}, ensure_ascii=False, separators=(",", ":"), sort_keys=True),
            }

        for y in sorted(frentes_by_year):
            fids = sorted(set(frentes_by_year[y]), key=int)

            async def w(fid: str, yy: int = y):
                return await fr_mem_worker(fid, yy)
            mem_rows, mem_errs = await bounded_gather_pbar(
                fids, w, concurrency=concurrency_frentes, description="camara:deputados_frentes",
            )
            if mem_errs:
                log.warning(f"[camara:frentes/membros] year={y} errors={len(mem_errs)}")
            if mem_rows:
                mp = write_relation_parts(
                    mem_rows, paths=paths, manifest=manifest,
                    source="camara", relation="frentes/membros", year=y,
                    part_rows=50_000, sort=True
                )
                fr_mem_count += len(mem_rows)
                log.info(f"[camara:frentes/membros] year={y} wrote {len(mem_rows)} rows in {len(mp)} part(s)")

    return dep_count, fr_det_count, fr_mem_count
