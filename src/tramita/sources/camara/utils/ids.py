# tramita/sources/camara/utils/ids.py

from typing import Any, Iterable

from tramita.http.client import HttpClient, HttpError
from tramita.sources.camara.client import camara_fetch


async def _list_ids_generic(
    hc: HttpClient,
    path: str,
    *,
    page_size: int = 100,
    id_fields: tuple[str, ...] = ("id",),
    extra_params: dict[str, Any] | None = None,
    supports_ordering: bool = True,
) -> list[str]:
    params: dict[str, Any] = {}
    if supports_ordering:
        params |= {"ordem": "ASC", "ordenarPor": "id"}
    if extra_params:
        params |= extra_params
    try:
        dados = await camara_fetch(
            hc, path, params, itens=page_size,
        )
    except HttpError as e:
        if supports_ordering and (e.status_code in (400, 422)):
            # retry without unsupported order params
            dados = await camara_fetch(
                hc, path, extra_params or {}, itens=page_size,
            )
        else:
            raise
    out: list[str] = []
    for d in dados or []:
        oid = next((d.get(f) for f in id_fields if d.get(f) is not None), None)
        if oid is None:
            continue
        try:
            out.append(str(int(oid)))
        except Exception:
            out.append(str(oid))
    try:
        return sorted(set(out), key=int)
    except Exception:
        return sorted(set(out), key=str)


async def _legislaturas_for_years(hc: HttpClient, years: Iterable[int]) -> list[str]:
    y0, y1 = min(years), max(years)
    dados = await camara_fetch(hc, "/legislaturas", {}, itens=100,)
    out: list[str] = []
    for it in dados or []:
        try:
            lid = str(int(it.get("id")))  # type: ignore
        except Exception:
            continue
        di = (it.get("dataInicio") or "")[:10]
        df = (it.get("dataFim") or "")[:10]
        try:
            yi = int(di[:4])
            yf = int(df[:4]) if df else yi
        except Exception:
            continue
        if not (yf < y0 or yi > y1):
            out.append(lid)
    return sorted(set(out), key=int)


async def _list_all_orgaos_ids(hc: HttpClient, *, page_size: int = 100) -> list[str]:
    """
    Enumerate every órgão id using /orgaos (paginated). Returns numeric-string ids, sorted.
    """
    dados = await camara_fetch(
        hc,
        "/orgaos",
        {"ordem": "ASC", "ordenarPor": "id"},
        itens=page_size,
        concurrency=8,
        fallback_follow_next=True,
    )
    ids: list[str] = []
    for d in dados or []:
        oid = d.get("id")
        if oid is None:
            oid = d.get("idOrgao")
        if oid is None:
            continue
        try:
            ids.append(str(int(oid)))
        except Exception:
            ids.append(str(oid))
    return sorted(set(ids), key=int)
