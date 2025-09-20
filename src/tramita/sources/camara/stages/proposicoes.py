# tramita/sources/camara/stages/proposicoes.py

from datetime import date
from typing import Iterable, Sequence
import pyarrow.parquet as pq

import logging


from tramita.config import settings
from tramita.http.client import HttpClient
from tramita.log import setup_logging
from tramita.sources.base import bounded_gather_pbar
from tramita.sources.camara.client import camara_fetch
from tramita.storage.manifest import SnapshotManifest
from tramita.storage.parquet import write_index_parquet, write_relation_parts
from tramita.storage.paths import BronzePaths
from tramita.sources.camara.utils.paging import _iter_date_windows, _hash_take, _parse_fraction
from tramita.sources.camara.utils.builders import _build_details_from_index
from tramita.sources.camara.utils.rows import _row

setup_logging()
log = logging.getLogger(__name__)


CAMARA_BASE = settings.camara_base_url.rstrip("/")

SIGLA_PROP_INCLUDES = [
    # Núcleo do processo legislativo
    "PL", "PLP", "PLC", "PLS", "PLN", "PLV", "PEC", "MPV", "PDC", "PDL", "PDN", "PDS",
    # Emendas e correlatos (mínimo útil para tramitação)
    "EMC",  # Emenda na Comissão
    "EMP",  # Emenda de Plenário
    "EMS",  # Emenda/Substitutivo do Senado
    "EMR",  # Emenda de Relator
    "ESB",  # Emenda ao Substitutivo
    "ERD",  # Emenda de Redação
    "EMA",  # Emenda Aglutinativa de Plenário
    "EAG",  # Emenda Substitutiva Aglutinativa Global
    "EPP",  # Emenda ao PPA
    "EMPV",  # Emenda à Medida Provisória (CN)
    # Substitutivos e subemendas
    "SBT",  # Substitutivo
    "SBE",  # Subemenda
    "ESP",  # Emenda Substitutiva de Plenário
    "SSP",  # Subemenda Substitutiva de Plenário
    # (opcionalmente, versões “-A” adotadas pela comissão)
    "SBT-A", "SBE-A", "EMC-A",
]


async def build_index_proposicoes_tramitadas(
    paths: BronzePaths,
    years: Iterable[int],
    *,
    window_days: int = 30,
    page_size: int = 100,
    concurrency_windows: int = 10,
    include_sigla: Sequence[str] | None = None,
    sample: str | None = None,  # e.g. "1/200"
    start_date: date | None = None,
    end_date: date | None = None,
) -> int:
    """
    Build the index of proposições that had *tramitação* between the first and last
    year in `years`, scanning 30-day windows. Dedup by id. Bucket by the year of the
    window where the id first appears (deterministic).
    """
    include_sigla = include_sigla or SIGLA_PROP_INCLUDES
    sigla_set = set(include_sigla) if include_sigla else None

    y0, y1 = min(years), max(years)
    start = start_date or date(y0, 1, 1)
    end = end_date or date(y1, 12, 31)
    windows = _iter_date_windows(start, end, days=window_days)
    keep_num, keep_den = _parse_fraction(sample)

    async with HttpClient(
        CAMARA_BASE,
        rate_per_sec=settings.camara_rate,
        timeout=settings.http_timeout,
        user_agent=settings.user_agent,
    ) as hc:
        async def worker(win: tuple[date, date]):
            d0, d1 = win
            base_params = {
                "dataInicio": d0.isoformat(),
                "dataFim": d1.isoformat(),
                "ordem": "ASC",
                "ordenarPor": "id",
            }
            all_rows: list[dict] = []
            if include_sigla:
                # Fetch each type separately (reduces payload upstream)
                for st in include_sigla:
                    params = base_params | {"siglaTipo": st}
                    dados = await camara_fetch(
                        hc, "/proposicoes", params,
                        itens=page_size,
                    )
                    all_rows.extend(dados)
            else:
                dados = await camara_fetch(
                    hc, "/proposicoes", base_params,
                    itens=page_size,
                )
                all_rows.extend(dados)
            return d0, d1, all_rows

        results, errs = await bounded_gather_pbar(
            windows, worker, concurrency=concurrency_windows, description="camara:proposicoes"
        )

    if errs:
        log.warning(
            f"[camara:index-tram] windows_errors={len(errs)} (continuing with successes)")

    # Deterministic order across windows
    results.sort(key=lambda r: (r[0], r[1]))

    # First-seen wins
    seen: set[str] = set()
    by_year: dict[int, list[dict]] = {}

    for d0, _, dados in results:
        bucket_year = d0.year
        for d in dados:
            if sigla_set is not None:
                if (d.get("siglaTipo") or "") not in sigla_set:
                    continue
            pid = str(d["id"])
            # optional: sampling
            if not _hash_take(pid, keep_num, keep_den):
                continue
            if pid in seen:
                continue
            seen.add(pid)
            url = d.get("uri") or f"{CAMARA_BASE}/proposicoes/{pid}"
            row = {
                "source": "camara",
                "entity": "proposicoes",
                # note: bucket year (first-seen tramitação window)
                "year": bucket_year,
                "id": pid,
                "url": url,
            }
            by_year.setdefault(bucket_year, []).append(row)

    total = 0
    for y in sorted(by_year):
        idx_path = paths.index_file("camara", "proposicoes", y)
        n = write_index_parquet(by_year[y], idx_path)
        log.info(f"[camara:index-tram] year={y} proposicoes={n} -> {idx_path}")
        total += n

    log.info(
        f"[camara:index-tram] total_unique_ids={len(seen)} across years {y0}-{y1}")
    return total


async def expand_index_via_relacionadas(
    paths: BronzePaths,
    manifest: SnapshotManifest,
    years: Iterable[int],
    *,
    concurrency: int = 16,
    max_rounds: int = 6,
    include_sigla: Sequence[str] | None = None,
) -> int:
    """
    Iteratively follow /proposicoes/{id}/relacionadas from the current index until
    no new proposicoes are found. For each origin id we write one relation row under
    camara/relacionadas/year=YYYY/. Any newly discovered proposicao ids are bucketed
    deterministically into the origin's year (first-seen wins), merged back into the
    per-year index parquet, and may trigger further rounds.

    Returns total number of *new* proposicoes added across all rounds.
    """
    include_sigla = include_sigla or SIGLA_PROP_INCLUDES
    sigla_set = set(include_sigla) if include_sigla else None

    id_year: dict[str, int] = {}
    for y in years:
        idx_path = paths.index_file("camara", "proposicoes", y)
        if not idx_path.exists():
            continue
        t = pq.read_table(idx_path, columns=["id"])
        for r in t.to_pylist():
            pid = str(r["id"])
            id_year.setdefault(pid, y)  # keep first bucket for determinism

    if not id_year:
        log.info("[camara:relacionadas] no seed ids in index; skipping expansion")
        return 0

    # Track which ids we've already fetched /relacionadas for in THIS run
    fetched: set[str] = set()
    total_new = 0

    async with HttpClient(
        CAMARA_BASE,
        rate_per_sec=settings.camara_rate,
        timeout=settings.http_timeout,
        user_agent=settings.user_agent,
    ) as hc:

        async def rel_worker(pid: str, yy: int):
            path = f"/proposicoes/{pid}/relacionadas"
            dados = await camara_fetch(
                hc, path, {},
                itens=100,
            )
            # Collect new proposicao ids from 'dados'
            new_ids: list[str] = []
            for it in dados or []:
                if sigla_set is not None and (it.get("siglaTipo") or "") not in sigla_set:
                    continue
                try:
                    rid = str(int(it.get("id")))  # type: ignore
                except Exception:
                    rid = str(it.get("id"))
                if rid and (rid not in id_year):
                    new_ids.append(rid)

            # One relation row per origin
            row = _row(
                entity="relacionadas",
                year=yy,
                id=pid,
                url=CAMARA_BASE + path,
                dados=dados,
            )

            return row, new_ids

        # ---- 2) iterate rounds until fixed point or max_rounds ----
        for round_idx in range(1, max_rounds + 1):
            # frontier = all known ids that haven't had /relacionadas fetched yet
            frontier_by_year: dict[int, list[str]] = {}
            for pid, yy in id_year.items():
                if pid not in fetched:
                    frontier_by_year.setdefault(yy, []).append(pid)

            if not frontier_by_year:
                log.info("[camara:relacionadas] fixed point reached; no pending frontier")
                break

            frontier_size = sum(len(v) for v in frontier_by_year.values())
            log.info(f"[camara:relacionadas] round={round_idx} frontier={frontier_size}")

            newly_found_by_year: dict[int, list[str]] = {}

            # process frontier grouped by the bucket year of the origin
            for y in sorted(frontier_by_year):
                ids = frontier_by_year[y]

                async def rel_id_worker(pid: str, yy: int = y):
                    return await rel_worker(pid, yy)

                results, errs = await bounded_gather_pbar(
                    ids, rel_id_worker, concurrency=concurrency, description="camara:proposicoes_relacionadas"
                )
                if errs:
                    log.warning(f"[camara:relacionadas] year={y} relation_errors={len(errs)}")

                # split (row, new_ids) → write rows + accumulate new ids
                rel_rows = []
                new_ids_accum: list[str] = []
                for row, new_ids in results:
                    rel_rows.append(row)
                    new_ids_accum.extend(new_ids)

                # write relation rows for this origin-year
                parts = write_relation_parts(
                    rel_rows,
                    paths=paths,
                    manifest=manifest,   # manifest from outer scope; will exist where this is called
                    source="camara",
                    relation="relacionadas",
                    year=y,
                    part_rows=50_000,
                    sort=True,
                )
                log.info(f"[camara:relacionadas] year={y} wrote {len(rel_rows)} rows in {len(parts)} part(s)")

                # mark fetched
                fetched.update(ids)

                # bucket new ids into *origin* year (first-seen wins)
                if new_ids_accum:
                    for rid in new_ids_accum:
                        if rid not in id_year:
                            id_year[rid] = y
                            newly_found_by_year.setdefault(y, []).append(rid)

            if not newly_found_by_year:
                log.info(f"[camara:relacionadas] round={round_idx} found no new ids; stopping")
                break

            # ---- 3) merge new ids into per-year index parquet ----
            for y, new_list in newly_found_by_year.items():
                idx_path = paths.index_file("camara", "proposicoes", y)
                existing: list[dict] = []
                if idx_path.exists():
                    t = pq.read_table(idx_path)
                    existing = [{**r, "year": y} for r in t.to_pylist()]

                have = {str(r["id"]) for r in existing}
                additions = []
                for pid in new_list:
                    if pid not in have:
                        additions.append({
                            "source": "camara",
                            "entity": "proposicoes",
                            "year": y,
                            "id": pid,
                            "url": f"{CAMARA_BASE}/proposicoes/{pid}",
                        })

                if additions:
                    merged = existing + additions
                    # write deterministically (function sorts)
                    n = write_index_parquet(merged, idx_path)
                    log.info(f"[camara:index-rel] year={y} merged index → {n} ids ({len(additions)} new)")

            round_new = sum(len(v) for v in newly_found_by_year.values())
            total_new += round_new

    log.info(f"[camara:relacionadas] total_new_ids={total_new}")
    return total_new


async def build_details_proposicoes(
    paths: BronzePaths,
    manifest: SnapshotManifest,
    year: int,
    *,
    concurrency: int = 20
) -> int:
    # Favor stored URL from the index, but provide a canonical fallback
    return await _build_details_from_index(
        paths=paths,
        manifest=manifest,
        source="camara",
        index_entity="proposicoes",
        details_entity="proposicoes",
        year=year,
        endpoint_fmt="/proposicoes/{id}",
        concurrency=concurrency,
    )
