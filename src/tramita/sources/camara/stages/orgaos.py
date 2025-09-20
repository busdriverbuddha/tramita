# tramita/sources/camara/stages/orgaos.py

from typing import Iterable

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
from tramita.sources.camara.utils.ids import _list_all_orgaos_ids

log = logging.getLogger(__name__)


CAMARA_BASE = settings.camara_base_url.rstrip("/")


async def build_all_orgaos(
    paths: BronzePaths,
    manifest: SnapshotManifest,
    *,
    page_size: int = 100,
    list_concurrency: int = 8,
    fetch_concurrency: int = 16,
    year_bucket: int = 0,
) -> int:
    """
    Fetch the full órgão catalog:
      1) GET /orgaos with pagination to enumerate ids.
      2) GET /orgaos/{id} for each id (concurrently).
    Store under camara/orgaos/details/year=0000/.
    Returns number of órgãos written.
    """
    setup_logging()

    async with HttpClient(
        CAMARA_BASE,
        rate_per_sec=settings.camara_rate,
        timeout=settings.http_timeout,
        user_agent=settings.user_agent,
    ) as hc:
        # 1) List all órgãos (paginated)
        ids = await _list_all_orgaos_ids(hc, page_size=page_size)

        # 2) Fetch details for each órgão id
        async def worker(org_id: str) -> BronzeRow:
            url = f"/orgaos/{org_id}"
            dados = await camara_fetch(hc, url, None)
            return _row(
                entity="orgaos",
                year=year_bucket,
                id=org_id,
                url=CAMARA_BASE + url,
                dados=dados,
            )

        rows, errs = await bounded_gather(ids, worker, concurrency=fetch_concurrency)
        if errs:
            log.warning(f"[camara:orgaos(all)] detail_errors={len(errs)} (continuing with successes)")

    parts = write_details_parts(
        rows,
        paths=paths,
        manifest=manifest,
        source="camara",
        entity="orgaos",
        year=year_bucket,
        part_rows=50_000,
        sort=True,
    )

    log.info(f"[camara:orgaos(all)] wrote {len(rows)} rows in {len(parts)} part(s) → year={year_bucket:04d}")
    return len(rows)


async def build_orgaos_membros(
    paths: BronzePaths,
    manifest: SnapshotManifest,
    years: Iterable[int],
    *,
    page_size: int = 100,
    concurrency_orgaos: int = 16,
    year_bucket: int | None = None,
) -> int:
    """
    Fetch /orgaos/{id}/membros for all órgãos (paginated) and store one row per órgão
    under camara/orgaos/membros/year=YYYY/. Defaults to bucketing in the first year provided.
    """
    setup_logging()
    y0 = min(years) if years else 0
    bucket = y0 if year_bucket is None else year_bucket
    total = 0

    async with HttpClient(
        CAMARA_BASE,
        rate_per_sec=settings.camara_rate,
        timeout=settings.http_timeout,
        user_agent=settings.user_agent,
    ) as hc:
        org_ids = await _list_all_orgaos_ids(hc, page_size=page_size)

        async def worker(oid: str) -> BronzeRow:
            dados = await camara_fetch(
                hc,
                f"/orgaos/{oid}/membros",
                {},  # relies on pagination links; no date filters documented here
                itens=page_size,
            )
            return _row(
                entity="orgaos/membros",
                year=bucket,
                id=oid,
                url=f"{CAMARA_BASE}/orgaos/{oid}/membros",
                dados=dados,
            )

        rows, errs = await bounded_gather(org_ids, worker, concurrency=concurrency_orgaos)
        if errs:
            log.warning(f"[camara:orgaos/membros] errors={len(errs)} (continuing with successes)")

    if rows:
        parts = write_relation_parts(
            rows,
            paths=paths,
            manifest=manifest,
            source="camara",
            relation="orgaos/membros",
            year=bucket,
            part_rows=50_000,
            sort=True,
        )
        total = len(rows)
        log.info(f"[camara:orgaos/membros] year={bucket} wrote {total} rows in {len(parts)} part(s)")

    return total


async def build_orgaos_votacoes_relations(
    paths: BronzePaths,
    manifest: SnapshotManifest,
    years: Iterable[int],
    *,
    page_size: int = 100,
    concurrency_orgaos: int = 12,
    year_bucket: int | None = None,
) -> int:
    """
    Fetch /orgaos/{id}/votacoes (paginated) for all órgãos and store one row per órgão
    under camara/orgaos/votacoes/year=YYYY/. Useful as an auxiliary discovery path for votação ids.
    """
    setup_logging()
    y0 = min(years) if years else 0
    bucket = y0 if year_bucket is None else year_bucket
    total = 0

    async with HttpClient(
        CAMARA_BASE,
        rate_per_sec=settings.camara_rate,
        timeout=settings.http_timeout,
        user_agent=settings.user_agent,
    ) as hc:
        org_ids = await _list_all_orgaos_ids(hc, page_size=page_size)

        async def worker(oid: str) -> BronzeRow:
            dados = await camara_fetch(
                hc,
                f"/orgaos/{oid}/votacoes",
                {"ordem": "ASC", "ordenarPor": "id"},
                itens=page_size,
            )
            return _row(
                entity="orgaos/votacoes",
                year=bucket,
                id=oid,
                url=f"{CAMARA_BASE}/orgaos/{oid}/votacoes",
                dados=dados,
            )

        rows, errs = await bounded_gather(org_ids, worker, concurrency=concurrency_orgaos)
        if errs:
            log.warning(f"[camara:orgaos/votacoes] errors={len(errs)} (continuing)")

    if rows:
        parts = write_relation_parts(
            rows,
            paths=paths,
            manifest=manifest,
            source="camara",
            relation="orgaos/votacoes",
            year=bucket,
            part_rows=50_000,
            sort=True,
        )
        total = len(rows)
        log.info(f"[camara:orgaos/votacoes] year={bucket} wrote {total} rows in {len(parts)} part(s)")

    return total
