# tramita/pipelines/bronze.py

import asyncio
from typing import Iterable

from tramita.log import setup_logging
from tramita.storage.paths import BronzePaths
from tramita.storage.manifest import new_manifest, SnapshotManifest
from tramita.sources.camara.stages.proposicoes import (
    build_index_proposicoes_tramitadas,
    expand_index_via_relacionadas,
    build_details_proposicoes,
)
from tramita.sources.camara.stages.temas import build_temas_relations
from tramita.sources.camara.stages.tramitacoes import build_tramitacoes_relations_and_orgaos
from tramita.sources.camara.stages.frentes import build_frentes_via_deputados
from tramita.sources.camara.stages.votacoes import build_votacoes_votos_orientacoes
from tramita.sources.camara.stages.eventos import (
    build_details_eventos,
    build_eventos_relations,
    expand_index_eventos_via_orgaos,
    build_index_eventos,
)

from tramita.sources.camara.stages.orgaos import (
    build_all_orgaos,
    build_orgaos_membros,
    build_orgaos_votacoes_relations,
)

from tramita.sources.camara.stages.deputados import (
    build_deputados_catalog,
    build_deputados_relations,
)

from tramita.sources.camara.stages.autores import build_autores_relations_and_entities

from tramita.sources.camara.stages.partidos import build_partidos_blocos_frentes_legislaturas


from tramita.sources.camara.referencias import (
    build_camara_referencias,
)

from tramita.sources.senado.stages.processos import (
    build_index_processos as build_index_processos_senado,
    build_details_processos_iterative as build_details_processos_iterative_senado,
    build_votacoes_relations as build_votacoes_relations_senado,
    build_emendas_relations as build_emendas_relations_senado,
    build_relatorias_relations as build_relatorias_relations_senado,
)

from tramita.sources.senado.stages.colegiados import (
    build_colegiados as build_colegiados_senado,
    build_colegiados_votacoes as build_colegiados_votacoes_senado,
)

from tramita.sources.senado.stages.parlamentares import (
    build_index_parlamentares_via_autoria as build_index_parlamentares_via_autoria_senado,
    build_index_parlamentares_via_legislaturas as build_index_parlamentares_via_legislaturas_senado,
    build_details_parlamentares as build_details_parlamentares_senado,
)

from tramita.sources.senado.stages.blocos import (
    build_blocos_details as build_blocos_details_senado,
    build_rel_bloco_partido as build_rel_bloco_partido_senado,
)

from tramita.sources.senado.stages.partidos import (
    build_partidos_details as build_partidos_details_senado
)


def _parse_years(years: str) -> list[int]:
    years = years.strip()
    if "-" in years:
        a, b = years.split("-", 1)
        return list(range(int(a), int(b) + 1))
    return [int(y) for y in years.split(",") if y.strip()]


async def bronze_camara(
    paths: BronzePaths,
    years: Iterable[int],
    *,
    types: list[str] | None = None,
    sample: str | None = None,
    window_days: int = 30,
    page_size: int = 100,
    start: str | None = None,
    end: str | None = None,
    autores: bool = True,
    resume_from: str = "all",
) -> None:
    setup_logging()
    try:
        manifest = SnapshotManifest.model_validate_json(paths.manifest_json.read_text())
    except FileNotFoundError:
        manifest = new_manifest(snapshot_name=paths.root.name, app_version="0.1.0")

    paths.ensure_base_dirs()
    paths.set_latest_symlink()

    order = [
        "index_tram", "expand_rel", "details_props", "temas",
        "tramitacoes", "frentes", "votacoes",
        "eventos_index1", "eventos_details1", "eventos_rel1",
        "eventos_expand_orgaos", "eventos_index2", "eventos_details2", "eventos_rel2",
        "orgaos_all", "orgaos_membros", "orgaos_votacoes",
        "autores", "referencias", "deputados_catalog", "deputados_relations",
        "pblf"  # partidos/blocos/frentes/legislaturas
    ]
    start_idx = order.index(resume_from) if resume_from != "all" else 0

    def should(stage: str) -> bool:
        return order.index(stage) >= start_idx

    # 1) Index stage (tramitação windows)
    from datetime import date
    start_d = date.fromisoformat(start) if start else None
    end_d = date.fromisoformat(end) if end else None

    if should("index_tram"):
        await build_index_proposicoes_tramitadas(
            paths, years,
            window_days=window_days,
            page_size=page_size,
            concurrency_windows=4,
            include_sigla=types or None,
            sample=sample or None,
            start_date=start_d,
            end_date=end_d,
        )
    if should("expand_rel"):
        await expand_index_via_relacionadas(paths, manifest, years, concurrency=16, max_rounds=1)
    # 2) Details stage (unchanged)

    if should("details_props"):
        for y in years:
            await build_details_proposicoes(paths, manifest, y, concurrency=20)

    if should("temas"):
        await build_temas_relations(paths, manifest, years, concurrency_props=16)

    if should("tramitacoes"):
        await build_tramitacoes_relations_and_orgaos(
            paths, manifest, years,
            concurrency_props=12,
            concurrency_orgaos=8,
            concurrency_deputados=16,
        )

    if should("frentes"):
        await build_frentes_via_deputados(
            paths, manifest, years,
            page_size=page_size,
            concurrency_deputados=16,
            concurrency_frentes=16,
        )

    if should("votacoes"):
        await build_votacoes_votos_orientacoes(
            paths, manifest, years,
            page_size=page_size,
            concurrency_props=12,
            concurrency_children=16,
        )

    if should("eventos_index1"):
        await build_index_eventos(
            paths, years,
            window_days=window_days,
            page_size=page_size,
            concurrency_windows=4,
            start_date=start_d, end_date=end_d,
        )

    if should("eventos_details1"):
        for y in years:
            await build_details_eventos(paths, manifest, y, concurrency=20)

    if should("eventos_rel1"):
        await build_eventos_relations(
            paths, manifest, years,
            page_size=page_size,
            concurrency_events=16,
        )

    if should("eventos_expand_orgaos"):
        await expand_index_eventos_via_orgaos(
            paths, years,
            window_days=window_days,
            page_size=page_size,
            concurrency_windows=4,
            concurrency_orgaos=12,
            start_date=start_d, end_date=end_d,
        )

    if should("eventos_index2"):
        await build_index_eventos(
            paths, years,
            window_days=window_days,
            page_size=page_size,
            concurrency_windows=4,
            start_date=start_d, end_date=end_d,
        )

    if should("eventos_details2"):
        for y in years:
            await build_details_eventos(paths, manifest, y, concurrency=20)

    if should("eventos_rel2"):
        await build_eventos_relations(
            paths, manifest, years,
            page_size=page_size,
            concurrency_events=16,
        )

    if should("orgaos_all"):
        await build_all_orgaos(
            paths, manifest,
            page_size=page_size,
            list_concurrency=8,
            fetch_concurrency=16,
            year_bucket=0,
        )

    if should("orgaos_membros"):
        # --- Órgãos relations: membros + votações ---
        await build_orgaos_membros(
            paths, manifest, years,
            page_size=page_size,
            concurrency_orgaos=16,
            year_bucket=min(years),
        )
    if should("orgaos_votacoes"):
        await build_orgaos_votacoes_relations(
            paths, manifest, years,
            page_size=page_size,
            concurrency_orgaos=12,
            year_bucket=min(years),
        )
    if should("autores") and autores:
        await build_autores_relations_and_entities(
            paths, manifest, years,
            page_size=page_size,
            concurrency_props=16,
            concurrency_deputados=16,
            concurrency_orgaos=8,
            fetch_deputados=True,
            fetch_orgaos=False,
        )
    if should("referencias"):
        await build_camara_referencias(paths, manifest, year_bucket=0)
    if should("deputados_catalog"):
        await build_deputados_catalog(
            paths, manifest,
            page_size=page_size,
            list_concurrency=8,
            fetch_concurrency=16,
            year_bucket=0,
        )
    if should("deputados_relations"):
        await build_deputados_relations(
            paths, manifest, years,
            page_size=page_size,
            concurrency_deputados=16,
        )
    if should("pblf"):
        # --- NEW: Partidos / Blocos / Frentes / Legislaturas ---
        await build_partidos_blocos_frentes_legislaturas(
            paths, manifest, years,
            page_size=page_size,
            list_concurrency=8,
            fetch_concurrency=16,
            concurrency_rel=16,
            year_bucket=0,
        )

    manifest.save(paths.manifest_json)


def run_bronze(
    source: str, years: str, snapshot: str, data_root: str = "./data",
    *, types: str = "", sample: str = "",
    window_days: int = 30, page_size: int = 100,
    start: str = "", end: str = "",
    autores: bool = True,
    resume_from: str = "all",
) -> None:
    p = BronzePaths(data_root=__import__("pathlib").Path(data_root), snapshot=snapshot)
    ys = _parse_years(years)
    if source not in ("all", "camara", "senado"):
        raise SystemExit(f"Unsupported source: {source}")
    if source in ("all", "camara"):
        typs = [t.strip() for t in types.split(",") if t.strip()] or None
        asyncio.run(bronze_camara(
            p, ys,
            types=typs, sample=sample or None,
            window_days=window_days, page_size=page_size,
            start=start or None, end=end or None,
            autores=autores,
            resume_from=resume_from,
        ))
    if source in ("senado", "all"):
        typs = [t.strip() for t in types.split(",") if t.strip()] or None
        asyncio.run(bronze_senado(
            p, ys,
            types=typs,
            window_days=window_days,
            page_size=page_size,
            resume_from=resume_from,
        ))


def verify_bronze(snapshot: str, data_root: str = "./data") -> int:
    from tramita.storage.manifest import verify_against_manifest, SnapshotManifest
    from pathlib import Path

    p = BronzePaths(data_root=Path(data_root), snapshot=snapshot)
    manifest = SnapshotManifest.model_validate_json(p.manifest_json.read_text())
    problems = verify_against_manifest(p.root, manifest)
    if problems:
        print("Verification problems:")
        for msg in problems:
            print(" -", msg)
        return 1
    print("OK: manifest matches files on disk.")
    return 0


async def bronze_senado(
    paths: BronzePaths,
    years: Iterable[int],
    *,
    types: list[str] | None = None,
    page_size: int = 100,  # currently unused (Senado often unpaginated)
    window_days: int = 30,
    resume_from: str = "all",
) -> None:
    """
    Initial Senado Bronze:
      1) index: /materias/pesquisa?ano=YYYY
      2) details: /materias/{id}
    """
    setup_logging()
    try:
        manifest = SnapshotManifest.model_validate_json(paths.manifest_json.read_text())
    except FileNotFoundError:
        manifest = new_manifest(snapshot_name=paths.root.name, app_version="0.1.0")

    paths.ensure_base_dirs()
    paths.set_latest_symlink()

    order = [
        "processos_index",
        "processos_details_iter",
        "processos_votacoes",
        "processos_emendas",
        "processos_relatorias",
        "colegiados",
        "colegiados_votacoes",
        "parlamentares_index",
        "parlamentares_details",
        "blocos",
        "partidos",
    ]
    start_idx = order.index(resume_from) if resume_from != "all" else 0

    def should(stage: str) -> bool:
        return order.index(stage) >= start_idx

    if should("processos_index"):
        await build_index_processos_senado(paths, years, tipo_siglas=types or None, window_days=window_days)

    if should("processos_details_iter"):
        await build_details_processos_iterative_senado(
            paths, manifest, years, concurrency=16, max_rounds=8
        )

    if should("processos_votacoes"):
        await build_votacoes_relations_senado(paths, manifest, years)

    if should("processos_emendas"):
        await build_emendas_relations_senado(paths, manifest, years)

    if should("processos_relatorias"):
        await build_relatorias_relations_senado(paths, manifest, years)

    if should("colegiados"):
        await build_colegiados_senado(paths, manifest, years)

    if should("colegiados_votacoes"):
        # iterate 30-day windows for each requested year (same window_days knob)
        await build_colegiados_votacoes_senado(
            paths, manifest, years, window_days=window_days
        )

    if should("parlamentares_index"):
        await build_index_parlamentares_via_autoria_senado(paths, years)
        await build_index_parlamentares_via_legislaturas_senado(paths, years)

    if should("parlamentares_details"):
        for yy in years:
            await build_details_parlamentares_senado(paths, manifest, yy)

    if should("blocos"):
        await build_blocos_details_senado(paths, manifest, years)
        await build_rel_bloco_partido_senado(paths, manifest, years)

    if should("partidos"):
        await build_partidos_details_senado(paths, manifest, years)

    manifest.save(paths.manifest_json)
