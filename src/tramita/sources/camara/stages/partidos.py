# tramita/sources/camara/stages/partidos.py

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
from tramita.sources.camara.utils.bucketing import _bucket_year_for_items
from tramita.sources.camara.utils.ids import _legislaturas_for_years, _list_ids_generic
from tramita.sources.camara.utils.rows import _row, BronzeRow

log = logging.getLogger(__name__)


CAMARA_BASE = settings.camara_base_url.rstrip("/")


async def build_partidos_blocos_frentes_legislaturas(
    paths: BronzePaths,
    manifest: SnapshotManifest,
    years: Iterable[int],
    *,
    page_size: int = 100,
    list_concurrency: int = 8,
    fetch_concurrency: int = 16,
    concurrency_rel: int = 16,
    year_bucket: int = 0,  # catálogos estáticos
) -> tuple[int, int]:
    """
    - Catálogos (detalhes) em year=0000:
        * /partidos, /blocos, /frentes, /legislaturas  -> GET {id}
    - Relações com variação temporal → bucket pelo 1º avistamento no intervalo:
        * partidos/{id}/membros, partidos/{id}/lideres
        * blocos/{id}/partidos
        * frentes/{id}/membros
        * legislaturas/{id}/lideres, legislaturas/{id}/mesa

    Returns (num_detail_rows, num_relation_rows)
    """
    setup_logging()
    details_written = 0
    relations_written = 0
    y0 = min(years) if years else 0
    default_bucket = y0

    async with HttpClient(
        CAMARA_BASE,
        rate_per_sec=settings.camara_rate,
        timeout=settings.http_timeout,
        user_agent=settings.user_agent,
    ) as hc:

        async def write_details(entity_name: str, base: str, id_fields: tuple[str, ...] = ("id",)):
            ids = await _list_ids_generic(
                hc, f"/{base}", page_size=page_size,
                id_fields=id_fields,
                extra_params={"idLegislatura": ",".join(leg_ids)} if base == "frentes" and leg_ids else None,
                supports_ordering=(base != "frentes"),
            )

            async def worker(eid: str) -> BronzeRow:
                url = f"/{base}/{eid}"
                dados = await camara_fetch(
                    hc, url, {},
                    itens=100,
                )
                return _row(
                    entity=entity_name,
                    year=year_bucket,
                    id=eid,
                    url=CAMARA_BASE + url,
                    dados=dados,
                )

            rows, errs = await bounded_gather(ids, worker, concurrency=fetch_concurrency)
            if errs:
                log.warning(f"[camara:{base}(all)] detail_errors={len(errs)}")
            parts = write_details_parts(
                rows,
                paths=paths,
                manifest=manifest,
                source="camara",
                entity=entity_name,
                year=year_bucket,
                part_rows=50_000,
                sort=True,
            )
            log.info(f"[camara:{base}(all)] wrote {len(rows)} rows in {len(parts)} part(s) → year={year_bucket:04d}")
            return len(rows), ids

        # ---- Details catalogs (year=0000) ----
        n_part, part_ids = await write_details("partidos", "partidos")
        n_bloc, bloc_ids = await write_details("blocos", "blocos")
        leg_ids = await _legislaturas_for_years(hc, years)
        n_frnt, frnt_ids = await write_details(
            "frentes", "frentes",
            ("id", "idFrente"),
            # pass params and skip ordering
        )
        n_leg, leg_ids = await write_details("legislaturas", "legislaturas")
        details_written = n_part + n_bloc + n_frnt + n_leg

        # ---- Relations (bucket by first-seen-in-interval) ----
        by_rel_year: dict[tuple[str, int], list[dict[str, Any]]] = {}

        async def add_relations_for_ids(base: str, ids: list[str], rels: list[str]):
            async def rel_worker(eid: str):
                out_rows: list[BronzeRow] = []
                for rel_suffix in rels:
                    dados = await camara_fetch(
                        hc, f"/{base}/{eid}/{rel_suffix}", {},
                        itens=page_size,
                    )
                    y = _bucket_year_for_items(dados, years, default_bucket)
                    rel_full = f"{base}/{rel_suffix}"
                    row = _row(
                        entity=rel_full,
                        year=y,
                        id=eid,
                        url=f"{CAMARA_BASE}/{base}/{eid}/{rel_suffix}",
                        dados=dados,
                    )
                    out_rows.append(row)
                return out_rows

            results, errs = await bounded_gather(ids, rel_worker, concurrency=concurrency_rel)
            if errs:
                log.warning(f"[camara:{base} relations] errors={len(errs)}")
            for rows in results:
                for row in rows:
                    key = (row["entity"], int(row["year"]))
                    by_rel_year.setdefault(key, []).append(row)

        # partidos: membros, lideres
        await add_relations_for_ids("partidos", part_ids, ["membros", "lideres"])
        # blocos: partidos
        await add_relations_for_ids("blocos",   bloc_ids, ["partidos"])
        # frentes: membros
        await add_relations_for_ids("frentes",  frnt_ids, ["membros"])
        # legislaturas: lideres, mesa
        await add_relations_for_ids("legislaturas", leg_ids, ["lideres", "mesa"])

    # write grouped relations
    for (rel, y), rows in sorted(by_rel_year.items(), key=lambda x: (x[0][0], x[0][1])):
        parts = write_relation_parts(
            rows,
            paths=paths,
            manifest=manifest,
            source="camara",
            relation=rel,  # e.g., "partidos/membros"
            year=y,
            part_rows=50_000,
            sort=True,
        )
        relations_written += len(rows)
        log.info(f"[camara:{rel}] year={y} wrote {len(rows)} rows in {len(parts)} part(s)")

    log.info(f"[camara:partidos+blocos+frentes+legislaturas] details={details_written} relations={relations_written}")
    return details_written, relations_written
