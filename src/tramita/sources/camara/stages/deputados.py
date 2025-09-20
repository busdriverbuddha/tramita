# tramita/sources/camara/stages/deputados.py

from typing import Any, Iterable

import logging


from tramita.config import settings
from tramita.http.client import HttpClient
from tramita.log import setup_logging
from tramita.sources.base import bounded_gather
from tramita.sources.camara.client import camara_fetch
from tramita.storage.manifest import SnapshotManifest
from tramita.storage.parquet import write_details_parts, write_relation_parts
from tramita.storage.paths import BronzePaths
from tramita.sources.camara.utils.rows import _row, BronzeRow
from tramita.sources.camara.utils.bucketing import _bucket_year_for_items
from tramita.sources.camara.utils.ids import _list_ids_generic

log = logging.getLogger(__name__)


CAMARA_BASE = settings.camara_base_url.rstrip("/")


async def build_deputados_catalog(
    paths: BronzePaths,
    manifest: SnapshotManifest,
    *,
    page_size: int = 100,
    list_concurrency: int = 8,
    fetch_concurrency: int = 16,
    year_bucket: int = 0,
) -> int:
    """
    Catálogo + detalhes de /deputados, estático em year=0000.
    """
    setup_logging()

    async with HttpClient(
        CAMARA_BASE,
        rate_per_sec=settings.camara_rate,
        timeout=settings.http_timeout,
        user_agent=settings.user_agent,
    ) as hc:
        ids = await _list_ids_generic(hc, "/deputados", page_size=page_size)

        async def worker(dep_id: str) -> BronzeRow:
            url = f"/deputados/{dep_id}"
            dados = await camara_fetch(hc, url, None, itens=page_size)
            return _row(
                entity="deputados",
                year=year_bucket,
                id=dep_id,
                url=CAMARA_BASE + url,
                dados=dados,
            )

        rows, errs = await bounded_gather(ids, worker, concurrency=fetch_concurrency)
        if errs:
            log.warning(f"[camara:deputados(all)] detail_errors={len(errs)} (continuing)")

    parts = write_details_parts(
        rows,
        paths=paths,
        manifest=manifest,
        source="camara",
        entity="deputados",
        year=year_bucket,
        part_rows=50_000,
        sort=True,
    )
    log.info(f"[camara:deputados(all)] wrote {len(rows)} rows in {len(parts)} part(s) → year={year_bucket:04d}")
    return len(rows)


async def build_deputados_relations(
    paths: BronzePaths,
    manifest: SnapshotManifest,
    years: Iterable[int],
    *,
    page_size: int = 100,
    concurrency_deputados: int = 16,
) -> tuple[int, int, int]:
    """
    Para cada deputado:
      - /deputados/{id}/orgaos      -> relation 'deputados/orgaos'
      - /deputados/{id}/historico   -> relation 'deputados/historico'
      - /deputados/{id}/frentes     -> relation 'deputados/frentes'
    Cada relação é bucketizada no 'primeiro avistamento' inferido das datas do payload.
    """
    setup_logging()
    y0 = min(years) if years else 0
    default_bucket = y0
    tot_orgs = tot_hist = tot_frentes = 0

    async with HttpClient(
        CAMARA_BASE,
        rate_per_sec=settings.camara_rate,
        timeout=settings.http_timeout,
        user_agent=settings.user_agent,
    ) as hc:
        dep_ids = await _list_ids_generic(hc, "/deputados", page_size=page_size)

        async def dep_worker(dep_id: str):
            async def fetch_rel(suffix: str) -> list[dict]:
                return await camara_fetch(hc, f"/deputados/{dep_id}/{suffix}", None, itens=page_size)

            dados_orgaos = await fetch_rel("orgaos")
            dados_histor = await fetch_rel("historico")
            dados_frentes = await fetch_rel("frentes")

            y_org = _bucket_year_for_items(dados_orgaos, years, default_bucket)
            y_hist = _bucket_year_for_items(dados_histor, years, default_bucket)
            y_frnt = _bucket_year_for_items(dados_frentes, years, default_bucket)

            def row(rel: str, y: int, data: list[dict]) -> BronzeRow:
                return _row(
                    entity=rel,
                    year=y,
                    id=dep_id,
                    url=f"{CAMARA_BASE}/deputados/{dep_id}/{rel.split('/', 1)[1]}",
                    dados=data,
                )

            return (
                row("deputados/orgaos", y_org, dados_orgaos),
                row("deputados/historico", y_hist, dados_histor),
                row("deputados/frentes", y_frnt, dados_frentes),
            )

        results, errs = await bounded_gather(dep_ids, dep_worker, concurrency=concurrency_deputados)
        if errs:
            log.warning(f"[camara:deputados→relations] errors={len(errs)}")

    # Group by (relation, year) to write deterministic part sets
    by_rel_year: dict[tuple[str, int], list[dict[str, Any]]] = {}
    for triple in results:
        for row in triple:
            key = (row["entity"], int(row["year"]))
            by_rel_year.setdefault(key, []).append(row)

    for (rel, y), rows in sorted(by_rel_year.items(), key=lambda x: (x[0][0], x[0][1])):
        parts = write_relation_parts(
            rows,
            paths=paths,
            manifest=manifest,
            source="camara",
            relation=rel,   # e.g., "deputados/orgaos"
            year=y,
            part_rows=50_000,
            sort=True,
        )
        if rel == "deputados/orgaos":
            tot_orgs += len(rows)
        elif rel == "deputados/historico":
            tot_hist += len(rows)
        elif rel == "deputados/frentes":
            tot_frentes += len(rows)
        log.info(f"[camara:{rel}] year={y} wrote {len(rows)} rows in {len(parts)} part(s)")

    log.info(f"[camara:deputados relations] orgaos={tot_orgs} historico={tot_hist} frentes={tot_frentes}")
    return tot_orgs, tot_hist, tot_frentes
