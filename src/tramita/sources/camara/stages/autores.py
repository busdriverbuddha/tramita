# tramita/sources/camara/stages/autores.py

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
from tramita.sources.camara.utils.rows import _row, BronzeRow
from tramita.sources.camara.utils.extractors import _extract_author_targets

log = logging.getLogger(__name__)


CAMARA_BASE = settings.camara_base_url.rstrip("/")


async def build_autores_relations_and_entities(
    paths: BronzePaths,
    manifest: SnapshotManifest,
    years: Iterable[int],
    *,
    page_size: int = 100,
    concurrency_props: int = 16,
    concurrency_deputados: int = 16,
    concurrency_orgaos: int = 8,
    fetch_orgaos: bool = True,
    fetch_deputados: bool = True,
) -> tuple[int, int, int]:
    """
    For each year, read proposicoes index, fetch autores relation, store one row per proposicao
    under camara/autores/year=YYYY/, and fetch unique /deputados/{id} and /orgaos/{id} details.

    Returns (n_rel_rows, n_deputados, n_orgaos).
    """
    setup_logging()
    total_rel = 0
    total_deps = 0
    total_orgs = 0

    # Track first-seen year for each author so we bucket details deterministically
    first_seen_dep: dict[str, int] = {}
    first_seen_org: dict[str, int] = {}

    import pyarrow.parquet as pq

    async with HttpClient(
        CAMARA_BASE,
        rate_per_sec=settings.camara_rate,
        timeout=settings.http_timeout,
        user_agent=settings.user_agent,
    ) as hc:

        # -------- 1) fetch autores per proposicao (by year) --------
        for y in years:
            idx_path = paths.index_file("camara", "proposicoes", y)
            if not idx_path.exists():
                log.warning(f"[camara:autores] missing index for year={y}: {idx_path}")
                continue

            table = pq.read_table(idx_path)
            ids = [str(r["id"]) for r in table.to_pylist()]

            async def rel_worker(pid: str):
                path = f"/proposicoes/{pid}/autores"
                # autores endpoint is NOT paginated; fetch once and read "dados"
                dados = await camara_fetch(hc, path, None, itens=page_size)

                # record first-seen author ids → bucket year
                deps, orgs = _extract_author_targets(dados)
                for d in deps:
                    first_seen_dep.setdefault(d, y)
                for o in orgs:
                    first_seen_org.setdefault(o, y)

                # store one relation row per proposicao (payload = {"dados":[...]} )
                return _row(
                    entity="autores",
                    year=y,
                    id=pid,
                    url=CAMARA_BASE + path,
                    dados=dados,
                )

            rel_rows, rel_errs = await bounded_gather_pbar(
                ids, rel_worker, concurrency=concurrency_props, description="camara:autores"
            )
            if rel_errs:
                log.warning(f"[camara:autores] year={y} relation_errors={len(rel_errs)}")

            # write relation parts (grouped under camara/autores/year=YYYY/)
            parts = write_relation_parts(
                rel_rows,
                paths=paths,
                manifest=manifest,
                source="camara",
                relation="autores",
                year=y,
                part_rows=50_000,
                sort=True,
            )
            total_rel += len(rel_rows)
            log.info(f"[camara:autores] year={y} wrote {len(rel_rows)} rows in {len(parts)} part(s)")

        # -------- 2) fetch unique author entities (deputados, orgaos) --------
        # We’ll bucket each entity into the first year it appeared above.
        # Build {year: [ids...]} for deterministic output.
        dep_by_year: dict[int, list[str]] = {}
        org_by_year: dict[int, list[str]] = {}
        for dep, y in first_seen_dep.items():
            dep_by_year.setdefault(y, []).append(dep)
        for org, y in first_seen_org.items():
            org_by_year.setdefault(y, []).append(org)

        async def dep_worker(yy: int, dep_id: str):
            url = f"/deputados/{dep_id}"
            dados = await camara_fetch(hc, url, None, itens=page_size)
            return _row(
                entity="deputados",
                year=yy,
                id=dep_id,
                url=CAMARA_BASE + url,
                dados=dados
            )

        async def org_worker(yy: int, org_id: str):
            url = f"/orgaos/{org_id}"
            dados = await camara_fetch(hc, url, None, itens=page_size)
            return _row(
                entity="orgaos",
                year=yy,
                id=org_id,
                url=CAMARA_BASE + url,
                dados=dados
            )

        # Deputados
        if fetch_deputados:
            for y in sorted(dep_by_year):
                dep_ids: list[str] = sorted(dep_by_year[y], key=int)

                async def dep_id_worker(dep_id: str, yy: int = y) -> BronzeRow:
                    return await dep_worker(yy, dep_id)

                dep_rows, dep_errs = await bounded_gather_pbar(
                    dep_ids,
                    dep_id_worker,
                    concurrency=concurrency_deputados,
                    description="camara:deputados"
                )
                if dep_errs:
                    log.warning(f"[camara:deputados] year={y} errors={len(dep_errs)}")
                parts = write_details_parts(
                    dep_rows,
                    paths=paths,
                    manifest=manifest,
                    source="camara",
                    entity="deputados",
                    year=y,
                    part_rows=50_000,
                    sort=True,
                )
                total_deps += len(dep_rows)
                log.info(f"[camara:deputados] year={y} wrote {len(dep_rows)} rows in {len(parts)} part(s)")

        # Órgãos
        if fetch_orgaos:
            for y in sorted(org_by_year):
                org_ids: list[str] = sorted(org_by_year[y], key=int)

                async def org_id_worker(org_id: str, yy: int = y) -> BronzeRow:
                    return await org_worker(yy, org_id)

                org_rows, org_errs = await bounded_gather_pbar(
                    org_ids,
                    org_id_worker,
                    concurrency=concurrency_orgaos,
                    description="camara:orgaos",
                )
                if org_errs:
                    log.warning(f"[camara:orgaos] year={y} errors={len(org_errs)}")
                parts = write_details_parts(
                    org_rows,
                    paths=paths,
                    manifest=manifest,
                    source="camara",
                    entity="orgaos",
                    year=y,
                    part_rows=50_000,
                    sort=True,
                )
                total_orgs += len(org_rows)
                log.info(f"[camara:orgaos] year={y} wrote {len(org_rows)} rows in {len(parts)} part(s)")

    log.info(f"[camara:autores] relations={total_rel} deputados={total_deps} orgaos={total_orgs}")
    return total_rel, total_deps, total_orgs
