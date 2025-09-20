# tramita/sources/camara/utils/builders.py

from typing import Iterable

import pyarrow.parquet as pq

import logging

from tramita.config import settings
from tramita.http.client import HttpClient
from tramita.log import setup_logging
from tramita.sources.base import bounded_gather
from tramita.sources.camara.client import camara_fetch
from tramita.storage.manifest import SnapshotManifest
from tramita.storage.paths import BronzePaths
from tramita.storage.parquet import write_relation_parts, write_details_parts
from tramita.sources.camara.utils.rows import _row, BronzeRow

log = logging.getLogger(__name__)


CAMARA_BASE = settings.camara_base_url.rstrip("/")


async def _build_simple_relation(
    paths: BronzePaths,
    manifest: SnapshotManifest,
    years: Iterable[int],
    *,
    relation: str,                 # "temas" | "tramitacoes"
    endpoint_fmt: str,             # e.g. "/proposicoes/{pid}/temas"
    concurrency_props: int = 16,
) -> int:
    """
    Generic helper: for each year, read proposicoes index and fetch a single
    non-paginated relation endpoint; store one row per proposicao under
    camara/<relation>/year=YYYY/.
    Returns total relation rows written.
    """
    import pyarrow.parquet as pq
    setup_logging()
    total_rel = 0

    async with HttpClient(
        CAMARA_BASE,
        rate_per_sec=settings.camara_rate,
        timeout=settings.http_timeout,
        user_agent=settings.user_agent,
    ) as hc:
        for y in years:
            idx_path = paths.index_file("camara", "proposicoes", y)
            if not idx_path.exists():
                log.warning(f"[camara:{relation}] missing index for year={y}: {idx_path}")
                continue

            table = pq.read_table(idx_path)
            ids = [str(r["id"]) for r in table.to_pylist()]

            async def rel_worker(pid: str) -> BronzeRow:
                path = endpoint_fmt.format(pid=pid)
                dados = await camara_fetch(
                    hc, path, {},
                    itens=100,
                )

                return _row(
                    entity=relation,
                    year=y,
                    id=pid,
                    url=CAMARA_BASE + path,
                    dados=dados,
                )

            rel_rows, rel_errs = await bounded_gather(ids, rel_worker, concurrency=concurrency_props)
            if rel_errs:
                log.warning(f"[camara:{relation}] year={y} relation_errors={len(rel_errs)}")

            parts = write_relation_parts(
                rel_rows,
                paths=paths,
                manifest=manifest,
                source="camara",
                relation=relation,
                year=y,
                part_rows=50_000,
                sort=True,
            )
            total_rel += len(rel_rows)
            log.info(f"[camara:{relation}] year={y} wrote {len(rel_rows)} rows in {len(parts)} part(s)")

    log.info(f"[camara:{relation}] total_rows={total_rel}")
    return total_rel


async def _build_details_from_index(
    *,
    paths: BronzePaths,
    manifest: SnapshotManifest,
    source: str,              # "camara"
    index_entity: str,        # "eventos" | "proposicoes" | ...
    details_entity: str,      # usually same as index_entity
    year: int,
    endpoint_fmt: str | None = None,  # e.g. "/eventos/{id}" (fallback to stored URL if None)
    concurrency: int = 20,
) -> int:
    """
    Generic: read ids.parquet for (source,index_entity,year), fetch details for each id,
    and write details parts under .../<details_entity>/details/year=YYYY/.
    Returns rows written.
    """
    idx_path = paths.index_file(source, index_entity, year)
    if not idx_path.exists():
        log.warning(f"[{source}:{details_entity}-details] missing index for year={year}: {idx_path}")
        return 0

    table = pq.read_table(idx_path)
    # keep both id and url if present; url (when present) is authoritative
    recs: list[dict] = [{"id": str(r["id"]), "url": r.get("url")} for r in table.to_pylist()]

    async with HttpClient(
        CAMARA_BASE,
        rate_per_sec=settings.camara_rate,
        timeout=settings.http_timeout,
        user_agent=settings.user_agent,
    ) as hc:

        async def worker(rec: dict) -> BronzeRow:
            eid = rec["id"]
            # prefer stored URL; else build from endpoint_fmt; else canonical default
            if rec.get("url"):
                path = rec["url"].replace(CAMARA_BASE, "")
            elif endpoint_fmt:
                path = endpoint_fmt.format(id=eid)
            else:
                path = f"/{details_entity}/{eid}"
            dados = await camara_fetch(
                hc, path, {},
                itens=100,
            )
            return _row(
                entity=details_entity,
                year=year,
                id=eid,
                url=CAMARA_BASE + path,
                dados=dados,
            )

        rows, errs = await bounded_gather(recs, worker, concurrency=concurrency)

    if errs:
        log.warning(f"[{source}:{details_entity}-details] year={year} errors={len(errs)}")

    parts = write_details_parts(
        rows,
        paths=paths,
        manifest=manifest,
        source=source,
        entity=details_entity,
        year=year,
        part_rows=50_000,
        sort=True,
    )
    log.info(f"[{source}:{details_entity}-details] year={year} wrote {len(rows)} rows in {len(parts)} part(s)")
    return len(rows)
