# tramita/pipelines/bronze.py

import asyncio
from typing import Iterable

from tramita.log import setup_logging
from tramita.storage.paths import BronzePaths
from tramita.storage.manifest import new_manifest
from tramita.sources.camara.pipelines import (
    build_autores_relations_and_entities,
    build_details_proposicoes,
    build_index_proposicoes_tramitadas,
    build_temas_relations,
    build_tramitacoes_relations,
    expand_index_via_relacionadas,
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
) -> None:
    setup_logging()
    manifest = new_manifest(snapshot_name=paths.root.name, app_version="0.1.0")
    paths.ensure_base_dirs()
    paths.set_latest_symlink()

    # 1) Index stage (tramitação windows)
    from datetime import date
    start_d = date.fromisoformat(start) if start else None
    end_d = date.fromisoformat(end) if end else None
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
    await expand_index_via_relacionadas(paths, manifest, years, concurrency=16, max_rounds=6)
    # 2) Details stage (unchanged)
    for y in years:
        await build_details_proposicoes(paths, manifest, y, concurrency=20)

    await build_temas_relations(paths, manifest, years, concurrency_props=16)
    await build_tramitacoes_relations(paths, manifest, years, concurrency_props=12)

    if autores:
        await build_autores_relations_and_entities(
            paths, manifest, years,
            page_size=page_size,
            concurrency_props=16,
            concurrency_deputados=16,
            concurrency_orgaos=8,
        )

    manifest.save(paths.manifest_json)


def run_bronze(
    source: str, years: str, snapshot: str, data_root: str = "./data",
    *, types: str = "", sample: str = "",
    window_days: int = 30, page_size: int = 100,
    start: str = "", end: str = "",
    autores: bool = True,
) -> None:
    p = BronzePaths(data_root=__import__("pathlib").Path(data_root), snapshot=snapshot)
    ys = _parse_years(years)
    if source in ("all", "camara"):
        typs = [t.strip() for t in types.split(",") if t.strip()] or None
        asyncio.run(bronze_camara(
            p, ys,
            types=typs, sample=sample or None,
            window_days=window_days, page_size=page_size,
            start=start or None, end=end or None,
            autores=autores,
        ))
    else:
        raise SystemExit(f"Unsupported source: {source}")


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