# tramita/sources/camara/stages/temas.py

from typing import Iterable

import logging


from tramita.config import settings
from tramita.storage.manifest import SnapshotManifest
from tramita.storage.paths import BronzePaths
from tramita.sources.camara.utils.builders import _build_simple_relation

log = logging.getLogger(__name__)


CAMARA_BASE = settings.camara_base_url.rstrip("/")


async def build_temas_relations(
    paths: BronzePaths,
    manifest: SnapshotManifest,
    years: Iterable[int],
    *,
    concurrency_props: int = 16,
) -> int:
    return await _build_simple_relation(
        paths, manifest, years,
        relation="temas",
        endpoint_fmt="/proposicoes/{pid}/temas",
        concurrency_props=concurrency_props,
    )
