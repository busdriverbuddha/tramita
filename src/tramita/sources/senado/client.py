# tramita/sources/senado/client.py

import json

from typing import Any

from tramita.http.client import HttpClient


def _dig(obj: Any, path: list[str]) -> Any:
    cur = obj
    for k in path:
        if isinstance(cur, dict) and k in cur:
            cur = cur[k]
        else:
            return None
    return cur


async def senado_fetch(hc: HttpClient, path: str, params: dict[str, Any]) -> dict:
    """
    GET Senado endpoint and return parsed JSON (dict or list wrapped into dict).
    Always requests JSON output. Keeps raw structure for Bronze.
    """
    p = params or {}
    text = await hc.get_text(path, params=p)
    try:
        obj = json.loads(text)
    except Exception as e:
        raise RuntimeError(f"Senado JSON decode error for {path}: {e}") from e
    # Normalize lists to a dict wrapper for consistent handling upstream
    if isinstance(obj, list):
        return {"_list": obj}
    return obj


async def senado_fetch_list(
    hc: HttpClient,
    path: str,
    params: dict[str, Any],
    *,
    candidates: list[list[str]] | None = None,
) -> list[dict]:
    """
    Fetch and try multiple nested paths until a list is found.

    Examples seen in the wild (kept liberal — we’ll tighten after confirming):
      - ["ListaMateria", "Materias", "Materia"]
      - ["Materias", "Materia"]
      - ["Materias"]
      - ["resultados"]
      - ["Itens"]

    Returns [] if nothing matches.
    """
    obj = await senado_fetch(hc, path, params)
    if candidates is None:
        candidates = [
            ["ListaMateria", "Materias", "Materia"],
            ["ListaMateria", "Materias"],
            ["Materias", "Materia"],
            ["Materias"],
            ["listaMaterias", "materias"],
            ["resultados"],
            ["Itens"],
            ["_list"],  # normalized list wrapper fallback
        ]
    for path_keys in candidates:
        val = _dig(obj, path_keys)
        if isinstance(val, list):
            return val  # type: ignore
    return []
