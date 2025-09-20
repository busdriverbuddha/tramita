# tramita/sources/camara/stages/votacoes.py

from typing import Iterable

import logging


from tramita.config import settings
from tramita.http.client import HttpClient
from tramita.log import setup_logging
from tramita.sources.base import bounded_gather_pbar
from tramita.sources.camara.client import camara_fetch
from tramita.storage.manifest import SnapshotManifest
from tramita.storage.parquet import write_relation_parts
from tramita.storage.paths import BronzePaths
from tramita.sources.camara.utils.rows import _row, BronzeRow

log = logging.getLogger(__name__)


CAMARA_BASE = settings.camara_base_url.rstrip("/")


async def build_votacoes_votos_orientacoes(
    paths: BronzePaths,
    manifest: SnapshotManifest,
    years: Iterable[int],
    *,
    page_size: int = 100,
    concurrency_props: int = 12,      # concurrent proposições -> /votacoes
    concurrency_children: int = 16,   # concurrent votações -> /votos + /orientacoes
) -> tuple[int, int, int]:
    """
    For each year bucket of proposições:
      - GET /proposicoes/{pid}/votacoes (paginated) and store one relation row per proposição
        under camara/votacoes/year=YYYY/ (payload = {"dados":[...]}).
      - Collect votação IDs discovered and, bucketed by the same proposição year,
        fetch all pages of:
          * GET /votacoes/{vid}/votos        -> store under camara/votos/year=YYYY/
          * GET /votacoes/{vid}/orientacoes  -> store under camara/orientacoes/year=YYYY/

    Returns (n_proposicao_votacoes_rows, n_votos_rows, n_orientacoes_rows).
    """
    import pyarrow.parquet as pq

    setup_logging()
    total_rel_rows = 0
    total_votos_rows = 0
    total_orients_rows = 0

    async with HttpClient(
        CAMARA_BASE,
        rate_per_sec=settings.camara_rate,
        timeout=settings.http_timeout,
        user_agent=settings.user_agent,
    ) as hc:
        # -------- 1) /proposicoes/{id}/votacoes per year (paginated) --------
        votacoes_by_year: dict[int, list[str]] = {}  # {year: [votacao_id,...]}
        for y in years:
            idx_path = paths.index_file("camara", "proposicoes", y)
            if not idx_path.exists():
                log.warning(f"[camara:votacoes] missing index for year={y}: {idx_path}")
                continue

            table = pq.read_table(idx_path)
            prop_ids: list[str] = [str(r["id"]) for r in table.to_pylist()]

            async def prop_worker(pid: str) -> BronzeRow:
                # Use pagination helper; order by id for determinism.
                dados = await camara_fetch(
                    hc,
                    f"/proposicoes/{pid}/votacoes",
                    {"ordem": "ASC", "ordenarPor": "id"},
                    itens=page_size,
                    concurrency=8,
                    fallback_follow_next=True,
                )
                # Collect votação IDs (string per docs)
                for it in dados or []:
                    vid = it.get("id")
                    if vid is None:
                        continue
                    votacoes_by_year.setdefault(y, []).append(str(vid))

                return _row(
                    entity="votacoes",
                    year=y,
                    id=pid,
                    url=f"{CAMARA_BASE}/proposicoes/{pid}/votacoes",
                    dados=dados,
                )

            rel_rows, rel_errs = await bounded_gather_pbar(
                prop_ids, prop_worker, concurrency=concurrency_props,
                description="camara:votacoes",
            )
            if rel_errs:
                log.warning(f"[camara:votacoes] year={y} relation_errors={len(rel_errs)}")

            parts = write_relation_parts(
                rel_rows,
                paths=paths,
                manifest=manifest,
                source="camara",
                relation="votacoes",
                year=y,
                part_rows=50_000,
                sort=True,
            )
            total_rel_rows += len(rel_rows)
            log.info(f"[camara:votacoes] year={y} wrote {len(rel_rows)} rows in {len(parts)} part(s)")

        # Normalize/unique votação IDs per year (deterministic order)
        for y in list(votacoes_by_year.keys()):
            vids = sorted(set(votacoes_by_year[y]))
            votacoes_by_year[y] = vids

        # -------- 2) For each votação id -> fetch votos + orientacoes (paginated) --------
        for y in sorted(votacoes_by_year.keys()):
            vid_list = votacoes_by_year[y]

            async def child_worker(vid: str):
                # Fetch both paginated lists serially per vid (bounded by concurrency_children across vids)
                votos = await camara_fetch(
                    hc,
                    f"/votacoes/{vid}/votos",
                    {},  # no special ordering documented beyond pagination; links drive order
                    itens=page_size,
                    concurrency=8,
                    fallback_follow_next=True,
                )
                orients = await camara_fetch(
                    hc,
                    f"/votacoes/{vid}/orientacoes",
                    {},
                    itens=page_size,
                    concurrency=8,
                    fallback_follow_next=True,
                )
                votos_row = _row(
                    entity="votos",
                    year=y,
                    id=str(vid),
                    url=f"{CAMARA_BASE}/votacoes/{vid}/votos",
                    dados=votos,
                )
                orients_row = _row(
                    entity="orientacoes",
                    year=y,
                    id=str(vid),
                    url=f"{CAMARA_BASE}/votacoes/{vid}/orientacoes",
                    dados=orients,
                )

                return votos_row, orients_row

            results, child_errs = await bounded_gather_pbar(
                vid_list, child_worker, concurrency=concurrency_children,
                description="camara:votos+orientacoes"
            )
            if child_errs:
                log.warning(f"[camara:votos+orientacoes] year={y} errors={len(child_errs)}")

            votos_rows = [r[0] for r in results]
            orient_rows = [r[1] for r in results]

            if votos_rows:
                vp = write_relation_parts(
                    votos_rows,
                    paths=paths,
                    manifest=manifest,
                    source="camara",
                    relation="votos",
                    year=y,
                    part_rows=50_000,
                    sort=True,
                )
                total_votos_rows += len(votos_rows)
                log.info(f"[camara:votos] year={y} wrote {len(votos_rows)} rows in {len(vp)} part(s)")

            if orient_rows:
                op = write_relation_parts(
                    orient_rows,
                    paths=paths,
                    manifest=manifest,
                    source="camara",
                    relation="orientacoes",
                    year=y,
                    part_rows=50_000,
                    sort=True,
                )
                total_orients_rows += len(orient_rows)
                log.info(f"[camara:orientacoes] year={y} wrote {len(orient_rows)} rows in {len(op)} part(s)")

    log.info(
        f"[camara:votacoes+votos+orientacoes] votacoes_rows={total_rel_rows} "
        f"votos_rows={total_votos_rows} orientacoes_rows={total_orients_rows}"
    )
    return total_rel_rows, total_votos_rows, total_orients_rows
