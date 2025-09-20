# tramita/sources/camara/stages/eventos.py

from datetime import date
from typing import Iterable

import logging


from tramita.config import settings
from tramita.http.client import HttpClient
from tramita.log import setup_logging
from tramita.sources.base import bounded_gather
from tramita.sources.camara.client import camara_fetch
from tramita.storage.manifest import SnapshotManifest
from tramita.storage.parquet import write_index_parquet, write_relation_parts
from tramita.storage.paths import BronzePaths
from tramita.sources.camara.utils.rows import _row, BronzeRow
from tramita.sources.camara.utils.paging import _iter_date_windows
from tramita.sources.camara.utils.builders import _build_details_from_index
from tramita.sources.camara.utils.ids import _list_all_orgaos_ids


log = logging.getLogger(__name__)


CAMARA_BASE = settings.camara_base_url.rstrip("/")


async def build_details_eventos(
    paths: BronzePaths,
    manifest: SnapshotManifest,
    year: int,
    *,
    concurrency: int = 20,
) -> int:
    return await _build_details_from_index(
        paths=paths,
        manifest=manifest,
        source="camara",
        index_entity="eventos",
        details_entity="eventos",
        year=year,
        endpoint_fmt="/eventos/{id}",
        concurrency=concurrency,
    )


async def build_eventos_relations(
    paths: BronzePaths,
    manifest: SnapshotManifest,
    years: Iterable[int],
    *,
    page_size: int = 100,
    concurrency_events: int = 16,
) -> tuple[int, int, int, int]:
    """
    For each evento id (per-year index), fetch the paginated relations:
      - /eventos/{id}/pauta         -> relation 'eventos/pauta'
      - /eventos/{id}/votacoes      -> relation 'eventos/votacoes'
      - /eventos/{id}/deputados     -> relation 'eventos/deputados'
      - /eventos/{id}/orgaos        -> relation 'eventos/orgaos'
    We write one row per evento for each relation (payload = {"dados":[...]}).
    Returns (#pauta_rows, #votacoes_rows, #deputados_rows, #orgaos_rows).
    """
    import pyarrow.parquet as pq
    setup_logging()

    total_pauta = total_vot = total_deps = total_orgs = 0

    async with HttpClient(
        CAMARA_BASE,
        rate_per_sec=settings.camara_rate,
        timeout=settings.http_timeout,
        user_agent=settings.user_agent,
    ) as hc:
        for y in years:
            idx_path = paths.index_file("camara", "eventos", y)
            if not idx_path.exists():
                log.warning(f"[camara:eventos-rel] missing index for year={y}: {idx_path}")
                continue

            table = pq.read_table(idx_path)
            eids: list[str] = [str(r["id"]) for r in table.to_pylist()]

            async def rel_worker(eid: str):
                async def fetch_list(path: str) -> list[dict]:
                    return await camara_fetch(hc, path, {}, itens=page_size)

                pauta = await fetch_list(f"/eventos/{eid}/pauta")
                ev_vot = await fetch_list(f"/eventos/{eid}/votacoes")
                deps = await fetch_list(f"/eventos/{eid}/deputados")
                orgs = await fetch_list(f"/eventos/{eid}/orgaos")

                def row(rel: str, data: list[dict]) -> BronzeRow:
                    return _row(
                        entity=rel,
                        year=y,
                        id=eid,
                        url=f"{CAMARA_BASE}/eventos/{eid}/{rel.split('/', 1)[1]}",
                        dados=data,
                    )

                return (
                    row("eventos/pauta", pauta),
                    row("eventos/votacoes", ev_vot),
                    row("eventos/deputados", deps),
                    row("eventos/orgaos", orgs),
                )

            results, errs = await bounded_gather(eids, rel_worker, concurrency=concurrency_events)
            if errs:
                log.warning(f"[camara:eventos-rel] year={y} errors={len(errs)}")

            pauta_rows = [r[0] for r in results]
            votacoes_rows = [r[1] for r in results]
            deputados_rows = [r[2] for r in results]
            orgaos_rows = [r[3] for r in results]

            if pauta_rows:
                pp = write_relation_parts(
                    pauta_rows, paths=paths, manifest=manifest,
                    source="camara", relation="eventos/pauta", year=y,
                    part_rows=50_000, sort=True,
                )
                total_pauta += len(pauta_rows)
                log.info(f"[camara:eventos/pauta] year={y} wrote {len(pauta_rows)} rows in {len(pp)} part(s)")

            if votacoes_rows:
                vp = write_relation_parts(
                    votacoes_rows, paths=paths, manifest=manifest,
                    source="camara", relation="eventos/votacoes", year=y,
                    part_rows=50_000, sort=True,
                )
                total_vot += len(votacoes_rows)
                log.info(f"[camara:eventos/votacoes] year={y} wrote {len(votacoes_rows)} rows in {len(vp)} part(s)")

            if deputados_rows:
                dp = write_relation_parts(
                    deputados_rows, paths=paths, manifest=manifest,
                    source="camara", relation="eventos/deputados", year=y,
                    part_rows=50_000, sort=True,
                )
                total_deps += len(deputados_rows)
                log.info(f"[camara:eventos/deputados] year={y} wrote {len(deputados_rows)} rows in {len(dp)} part(s)")

            if orgaos_rows:
                op = write_relation_parts(
                    orgaos_rows, paths=paths, manifest=manifest,
                    source="camara", relation="eventos/orgaos", year=y,
                    part_rows=50_000, sort=True,
                )
                total_orgs += len(orgaos_rows)
                log.info(f"[camara:eventos/orgaos] year={y} wrote {len(orgaos_rows)} rows in {len(op)} part(s)")

    log.info(
        f"[camara:eventos-rel] pauta={total_pauta} votacoes={total_vot} deputados={total_deps} orgaos={total_orgs}"
    )
    return total_pauta, total_vot, total_deps, total_orgs


async def expand_index_eventos_via_orgaos(
    paths: BronzePaths,
    years: Iterable[int],
    *,
    window_days: int = 30,
    page_size: int = 100,
    concurrency_windows: int = 4,
    concurrency_orgaos: int = 12,
    start_date: date | None = None,
    end_date: date | None = None,
) -> int:
    """
    Use /orgaos/{id}/eventos to discover evento IDs within date windows and merge
    them into camara/eventos/index/year=YYYY/ (bucket = window start year).
    Returns number of *new* evento ids added across all years.
    """
    setup_logging()
    y0, y1 = min(years), max(years)
    start = start_date or date(y0, 1, 1)
    end = end_date or date(y1, 12, 31)
    windows = _iter_date_windows(start, end, days=window_days)

    import pyarrow.parquet as pq

    # load existing index → {year: set(ids)}
    have: dict[int, set[str]] = {}
    for y in years:
        idx_path = paths.index_file("camara", "eventos", y)
        ids_y: set[str] = set()
        if idx_path.exists():
            t = pq.read_table(idx_path, columns=["id"])
            ids_y = {str(r["id"]) for r in t.to_pylist()}
        have[y] = ids_y

    total_new = 0

    async with HttpClient(
        CAMARA_BASE,
        rate_per_sec=settings.camara_rate,
        timeout=settings.http_timeout,
        user_agent=settings.user_agent,
    ) as hc:
        org_ids = await _list_all_orgaos_ids(hc, page_size=page_size)

        async def win_worker(win: tuple[date, date]):
            d0, d1 = win
            params = {
                "dataInicio": d0.isoformat(),
                "dataFim": d1.isoformat(),
                "ordem": "ASC",
                "ordenarPor": "id",
            }

            async def org_worker(oid: str) -> list[str]:
                itens = await camara_fetch(
                    hc, f"/orgaos/{oid}/eventos", params,
                    itens=page_size,
                )
                out: list[str] = []
                for it in itens or []:
                    vid = it.get("id")
                    if vid is None:
                        continue
                    try:
                        out.append(str(int(vid)))
                    except Exception:
                        out.append(str(vid))
                return out

            results, errs = await bounded_gather(org_ids, org_worker, concurrency=concurrency_orgaos)
            if errs:
                log.warning(f"[camara:orgaos→eventos] win={d0}..{d1} errors={len(errs)}")

            bucket_year = d0.year
            discovered = set(x for lst in results for x in lst)
            return bucket_year, discovered

        win_results, win_errs = await bounded_gather(windows, win_worker, concurrency=concurrency_windows)
        if win_errs:
            log.warning(f"[camara:orgaos→eventos] window_errors={len(win_errs)} (continuing)")

    # merge and write
    for y, discovered in sorted(win_results, key=lambda x: x[0]):
        if not discovered:
            continue
        idx_path = paths.index_file("camara", "eventos", y)
        existing = have.get(y, set())
        additions = sorted(discovered - existing, key=int if all(s.isdigit() for s in discovered) else str)
        if not additions:
            continue

        # rebuild full list for the year and write deterministically
        merged_rows = (
            [{"source": "camara", "entity": "eventos", "year": y, "id": pid, "url": f"{CAMARA_BASE}/eventos/{pid}"}]
            for pid
            in sorted(existing | discovered, key=int if all(s.isdigit() for s in existing | discovered) else str)
        )
        # materialize generator
        merged_rows = list(merged_rows)
        n = write_index_parquet(merged_rows, idx_path)  # type: ignore
        have[y] = existing | discovered
        total_new += len(additions)
        log.info(f"[camara:eventos-index<-orgaos] year={y} +{len(additions)} ids → {n} total")

    log.info(f"[camara:orgaos→eventos] total_new_eventos={total_new}")
    return total_new


async def build_index_eventos(
    paths: BronzePaths,
    years: Iterable[int],
    *,
    window_days: int = 30,
    page_size: int = 100,
    concurrency_windows: int = 4,
    start_date: date | None = None,
    end_date: date | None = None,
) -> int:
    """
    Scan /eventos using [dataInicio, dataFim] windows (like proposições),
    dedup by id, and bucket into the year of the window start (deterministic).
    Writes ids.parquet under camara/eventos/index/year=YYYY/.
    """
    setup_logging()

    y0, y1 = min(years), max(years)
    start = start_date or date(y0, 1, 1)
    end = end_date or date(y1, 12, 31)
    windows = _iter_date_windows(start, end, days=window_days)

    async with HttpClient(
        CAMARA_BASE,
        rate_per_sec=settings.camara_rate,
        timeout=settings.http_timeout,
        user_agent=settings.user_agent,
    ) as hc:
        async def worker(win: tuple[date, date]):
            d0, d1 = win
            params = {
                "dataInicio": d0.isoformat(),
                "dataFim": d1.isoformat(),
                "ordem": "ASC",
                "ordenarPor": "id",
            }
            dados = await camara_fetch(hc, "/eventos", params, itens=page_size)
            return d0, d1, dados

        results, errs = await bounded_gather(windows, worker, concurrency=concurrency_windows)

    if errs:
        log.warning(f"[camara:eventos-index] windows_errors={len(errs)} (continuing)")

    # Deterministic order across windows
    results.sort(key=lambda r: (r[0], r[1]))

    seen: set[str] = set()
    by_year: dict[int, list[dict]] = {}

    for d0, d1, dados in results:
        bucket_year = d0.year
        for d in dados or []:
            try:
                eid = str(int(d.get("id")))
            except Exception:
                eid = str(d.get("id"))
            if not eid or eid in seen:
                continue
            seen.add(eid)
            url = d.get("uri") or f"{CAMARA_BASE}/eventos/{eid}"
            by_year.setdefault(bucket_year, []).append({
                "source": "camara",
                "entity": "eventos",
                "year": bucket_year,
                "id": eid,
                "url": url,
            })

    total = 0
    for y in sorted(by_year):
        idx_path = paths.index_file("camara", "eventos", y)
        n = write_index_parquet(by_year[y], idx_path)
        log.info(f"[camara:eventos-index] year={y} eventos={n} -> {idx_path}")
        total += n

    log.info(f"[camara:eventos-index] total_unique_ids={len(seen)} across years {y0}-{y1}")
    return total
