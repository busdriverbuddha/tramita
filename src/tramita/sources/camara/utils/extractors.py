# tramita/sources/camara/utils/extractors.py

import re


_DEP_RE = re.compile(r"/deputados/(\d+)")
_ORG_RE = re.compile(r"/orgaos/(\d+)")
_FR_RE = re.compile(r"/frentes/(\d+)")


def _extract_frente_ids(items: list[dict]) -> set[str]:
    ids: set[str] = set()
    for it in items or []:
        for k in ("idFrente", "id"):
            if it.get(k) is not None:
                try:
                    ids.add(str(int(it[k])))
                except Exception:
                    ids.add(str(it[k]))
        for k in ("uri", "uriFrente"):
            u = it.get(k)
            if isinstance(u, str):
                m = _FR_RE.search(u)
                if m:
                    ids.add(m.group(1))
    return ids


def _extract_author_targets(items: list[dict]) -> tuple[set[str], set[str]]:
    """
    From autores items, return (deputados_ids, orgaos_ids) as strings.
    Tries URIs first; falls back to id fields when available.
    """
    deps: set[str] = set()
    orgs: set[str] = set()

    for a in items or []:
        # scan common URI-bearing keys
        for k in ("uri", "uriAutor", "urlAutor", "uriOrgao"):
            u = a.get(k)
            if isinstance(u, str):
                m = _DEP_RE.search(u)
                if m:
                    deps.add(m.group(1))
                m = _ORG_RE.search(u)
                if m:
                    orgs.add(m.group(1))
        # fallbacks if URIs are missing
        if "idAutor" in a and a["idAutor"] is not None:
            try:
                deps.add(str(int(a["idAutor"])))
            except Exception:
                pass
        if "codOrgaoAutor" in a and a["codOrgaoAutor"] is not None:
            # Câmara órgão codes are numeric in this API
            try:
                orgs.add(str(int(a["codOrgaoAutor"])))
            except Exception:
                pass
    return deps, orgs


def _extract_orgaos_from_tramitacoes(items: list[dict]) -> set[str]:
    """
    From tramitacoes 'dados', return órgão IDs found in 'uriOrgao'.
    """
    out: set[str] = set()
    for it in items or []:
        u = it.get("uriOrgao")
        if isinstance(u, str):
            m = _ORG_RE.search(u)
            if m:
                out.add(m.group(1))
    return out


def _extract_relatores_from_tramitacoes(items: list[dict]) -> set[str]:
    """
    From tramitacoes 'dados', return deputado IDs found in 'uriUltimoRelator'
    (fallback to 'uriRelator' if present).
    """
    out: set[str] = set()
    for it in items or []:
        for k in ("uriUltimoRelator", "uriRelator"):
            u = it.get(k)
            if isinstance(u, str):
                m = _DEP_RE.search(u)
                if m:
                    out.add(m.group(1))
    return out
