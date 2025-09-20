# tramita/sources/camara/referencias.py

import json
import logging
from typing import Any

from tramita.config import settings
from tramita.http.client import HttpClient
from tramita.log import setup_logging
from tramita.storage.manifest import SnapshotManifest
from tramita.storage.parquet import write_relation_parts
from tramita.storage.paths import BronzePaths
from tramita.sources.camara.client import camara_fetch
from tramita.sources.camara.utils.rows import _row, BronzeRow

log = logging.getLogger(__name__)

CAMARA_BASE = settings.camara_base_url.rstrip("/")

# You can add more endpoints here later (situacoesProposicao, tiposTramitacao, etc.)
REF_ENDPOINTS: dict[str, str] = {
    'deputados': '/referencias/deputados',
    'deputados_codSituacao': '/referencias/deputados/codSituacao',
    'deputados_codTipoProfissao': '/referencias/deputados/codTipoProfissao',
    'deputados_siglaUF': '/referencias/deputados/siglaUF',
    'deputados_tipoDespesa': '/referencias/deputados/tipoDespesa',
    'eventos': '/referencias/eventos',
    'eventos_codSituacaoEvento': '/referencias/eventos/codSituacaoEvento',
    'eventos_codTipoEvento': '/referencias/eventos/codTipoEvento',
    'orgaos': '/referencias/orgaos',
    'orgaos_codSituacao': '/referencias/orgaos/codSituacao',
    'orgaos_codTipoOrgao': '/referencias/orgaos/codTipoOrgao',
    'proposicoes': '/referencias/proposicoes',
    'proposicoes_codSituacao': '/referencias/proposicoes/codSituacao',
    'proposicoes_codTema': '/referencias/proposicoes/codTema',
    'proposicoes_codTipoAutor': '/referencias/proposicoes/codTipoAutor',
    'proposicoes_codTipoTramitacao': '/referencias/proposicoes/codTipoTramitacao',
    'proposicoes_siglaTipo': '/referencias/proposicoes/siglaTipo',
    'situacoesDeputado': '/referencias/situacoesDeputado'
}


async def build_camara_referencias(
    paths: BronzePaths,
    manifest: SnapshotManifest,
    *,
    year_bucket: int = 0,            # "static" bucket
    which: list[str] | None = None,  # None = all in REF_ENDPOINTS
) -> int:
    """
    Fetch selected Câmara reference endpoints and store one row per item as raw JSON
    under camara/referencias/<refname>/year=0000/.

    - entity name in manifest = "referencias/<refname>"
    - id = item["sigla"] if present, else item["cod"] (string)
    - url = canonical endpoint

    Returns total rows written across all references.
    """
    setup_logging()
    targets = which or list(REF_ENDPOINTS.keys())
    total_rows = 0

    async with HttpClient(
        CAMARA_BASE,
        rate_per_sec=settings.camara_rate,
        timeout=settings.http_timeout,
        user_agent=settings.user_agent,
    ) as hc:
        for refname in targets:
            path = REF_ENDPOINTS[refname]
            dados = await camara_fetch(hc, path, None)

            if not isinstance(dados, list):
                log.warning(
                    f"[camara:referencias] {refname} unexpected schema; storing nothing")
                continue

            rows: list[BronzeRow] = [
                _row(
                    entity=f"referencias/{refname}",
                    year=year_bucket,
                    id=_ref_id(it),
                    url=CAMARA_BASE + path,
                    dados=it,
                    wrap_dados=False,
                )
                for it in dados
            ]
            parts = write_relation_parts(
                rows,  # type: ignore
                paths=paths,
                manifest=manifest,
                source="camara",
                # path becomes camara/referencias/<refname>/year=0000/
                relation=f"referencias/{refname}",
                year=year_bucket,
                part_rows=50_000,
                sort=True,
            )
            total_rows += len(rows)
            log.info(
                f"[camara:referencias] {refname} wrote {len(rows)} rows in {len(parts)} part(s)")

    log.info(f"[camara:referencias] total_rows={total_rows}")
    return total_rows


def _to_str_id(v: Any) -> str:
    try:
        return str(int(v))
    except Exception:
        return str(v)


def _ref_id(it: Any) -> str:
    if isinstance(it, dict):
        if it.get("sigla"):
            return str(it["sigla"])
        if it.get("cod") is not None:
            return _to_str_id(it["cod"])
    # stable fallback
    return json.dumps(it, ensure_ascii=False, separators=(",", ":"), sort_keys=True)
