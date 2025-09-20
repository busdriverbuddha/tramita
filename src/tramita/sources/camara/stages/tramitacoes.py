# tramita/sources/camara/stages/tramitacoes.py

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
from tramita.sources.camara.utils.extractors import (
    _extract_orgaos_from_tramitacoes, _extract_relatores_from_tramitacoes,
)
from tramita.sources.camara.utils.rows import _row, BronzeRow


log = logging.getLogger(__name__)


CAMARA_BASE = settings.camara_base_url.rstrip("/")


async def build_tramitacoes_relations_and_orgaos(
    paths: BronzePaths,
    manifest: SnapshotManifest,
    years: Iterable[int],
    *,
    concurrency_props: int = 16,
    concurrency_orgaos: int = 8,
    concurrency_deputados: int = 16,
) -> tuple[int, int, int]:
    """
    Fetch /proposicoes/{id}/tramitacoes (relation rows) and, for every órgão
    referenced via 'uriOrgao', fetch /orgaos/{id} once; additionally, when a
    'uriUltimoRelator' is present, fetch the relator profile via /deputados/{id}.
    All entity fetches are bucketed by the origin proposição's first-seen year.

    Returns (n_relation_rows, n_orgaos_rows, n_deputados_rows).
    """
    import pyarrow.parquet as pq

    setup_logging()
    total_rel = 0
    total_orgs = 0
    total_deps = 0

    # Track first-seen bucket year for determinism
    first_seen_org: dict[str, int] = {}
    first_seen_dep: dict[str, int] = {}

    async with HttpClient(
        CAMARA_BASE,
        rate_per_sec=settings.camara_rate,
        timeout=settings.http_timeout,
        user_agent=settings.user_agent,
    ) as hc:
        # -------- 1) fetch tramitacoes per proposicao (by year) --------
        for y in years:
            idx_path = paths.index_file("camara", "proposicoes", y)
            if not idx_path.exists():
                log.warning(f"[camara:tramitacoes] missing index for year={y}: {idx_path}")
                continue

            table = pq.read_table(idx_path)
            ids = [str(r["id"]) for r in table.to_pylist()]

            async def rel_worker(pid: str) -> BronzeRow:
                path = f"/proposicoes/{pid}/tramitacoes"
                dados = await camara_fetch(
                    hc, path, {},
                    itens=100,
                )
                # collect órgãos and relatores referenced here and remember first-seen bucket year
                for org_id in _extract_orgaos_from_tramitacoes(dados):
                    first_seen_org.setdefault(org_id, y)
                for dep_id in _extract_relatores_from_tramitacoes(dados):
                    first_seen_dep.setdefault(dep_id, y)

                return _row(
                    entity="tramitacoes",
                    year=y,
                    id=pid,
                    url=CAMARA_BASE + path,
                    dados=dados,
                )

            rel_rows, rel_errs = await bounded_gather_pbar(
                ids, rel_worker, concurrency=concurrency_props,
                description="camara:tramitacoes"
            )
            if rel_errs:
                log.warning(f"[camara:tramitacoes] year={y} relation_errors={len(rel_errs)}")

            parts = write_relation_parts(
                rel_rows,
                paths=paths,
                manifest=manifest,
                source="camara",
                relation="tramitacoes",
                year=y,
                part_rows=50_000,
                sort=True,
            )
            total_rel += len(rel_rows)
            log.info(f"[camara:tramitacoes] year={y} wrote {len(rel_rows)} rows in {len(parts)} part(s)")

        # -------- 2) fetch unique órgão entities (grouped by first-seen year) --------
        org_by_year: dict[int, list[str]] = {}
        for org, y in first_seen_org.items():
            org_by_year.setdefault(y, []).append(org)

        for y in sorted(org_by_year):
            org_ids: list[str] = sorted(org_by_year[y], key=int)

            async def org_worker(org_id: str, yy: int = y) -> BronzeRow:
                url = f"/orgaos/{org_id}"
                dados = await camara_fetch(
                    hc, url, {},
                    itens=100,
                )
                return _row(
                    entity="orgaos",
                    year=yy,
                    id=org_id,
                    url=CAMARA_BASE + url,
                    dados=dados,
                )

            org_rows, org_errs = await bounded_gather_pbar(
                org_ids, org_worker, concurrency=concurrency_orgaos,
                description="camara:tramita_orgaos",
            )
            if org_errs:
                log.warning(f"[camara:orgaos<-tramitacoes] year={y} errors={len(org_errs)}")

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
            log.info(f"[camara:orgaos<-tramitacoes] year={y} wrote {len(org_rows)} rows in {len(parts)} part(s)")

        # -------- 3) fetch unique deputado entities (grouped by first-seen year) ------
        dep_by_year: dict[int, list[str]] = {}
        for dep, y in first_seen_dep.items():
            dep_by_year.setdefault(y, []).append(dep)

        for y in sorted(dep_by_year):
            dep_ids: list[str] = sorted(dep_by_year[y], key=int)

            async def dep_worker(dep_id: str, yy: int = y) -> BronzeRow:
                url = f"/deputados/{dep_id}"
                dados = await camara_fetch(
                    hc, url, {},
                    itens=100,
                )
                return _row(
                    entity="deputados",
                    year=yy,
                    id=dep_id,
                    url=CAMARA_BASE + url,
                    dados=dados,
                )

            dep_rows, dep_errs = await bounded_gather_pbar(
                dep_ids, dep_worker, concurrency=concurrency_deputados,
                description="camara:tramita_deputados",
            )
            if dep_errs:
                log.warning(f"[camara:deputados<-tramitacoes] year={y} errors={len(dep_errs)}")

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
            log.info(f"[camara:deputados<-tramitacoes] year={y} wrote {len(dep_rows)} rows in {len(parts)} part(s)")

    log.info(f"[camara:tramitacoes+orgaos+relatores] relations={total_rel} orgaos={total_orgs} deputados={total_deps}")
    return total_rel, total_orgs, total_deps
