# tramita/sources/camara/client.py

import json
import re
from typing import Any

from tramita.sources.base import bounded_gather_pbar
from tramita.http.client import HttpClient

_LAST_PAGE_RE = re.compile(r"[?&]pagina=(\d+)\b")


def _extract_last_page(links: list[dict]) -> int:
    for link in links or []:
        if (link.get("rel") or "").lower() == "last":
            href = link.get("href") or ""
            m = _LAST_PAGE_RE.search(href)
            if m:
                return int(m.group(1))
    return 1


def _has_next(links: list[dict]) -> bool:
    return any((link.get("rel") or "").lower() == "next" for link in (links or []))


async def camara_fetch(
    hc: HttpClient,
    path: str,
    params: dict[str, Any] | None,
    *,
    itens: int = 100,
    concurrency: int = 8,
    fallback_follow_next: bool = True,
) -> Any:
    """
    Fetch all rows under 'dados' from a Câmara endpoint.

    Rules:
      • First request is made WITHOUT pagina/itens (avoids 400 on non-paginated endpoints).
      • If links indicate pagination (next/last), re-fetch page 1 WITH pagina=1&itens=<itens>
        to ensure consistent sizing, then fetch remaining pages.
      • If 'last' exists, use it to fan out concurrently. Otherwise (only 'next' present),
        walk forward sequentially if fallback_follow_next=True.

    Returns concatenated list of items from 'dados' (or [] if absent).
    """
    params = params or {}
    # 1) Probe without page params (works for both non-paginated and paginated endpoints).
    text0 = await hc.get_text(path, params=params)
    obj0 = json.loads(text0)
    dados0 = obj0.get("dados")
    links0 = obj0.get("links") or []

    # Non-paginated (no next/last): return as-is.
    if not _has_next(links0) and _extract_last_page(links0) <= 1:
        return dados0 or ([] if isinstance(dados0, list) else {})

    # 2) Paginated: re-fetch page 1 with pagina/itens to standardize page size.
    base = dict(params)  # copy
    base.update({"pagina": 1, "itens": itens})

    text1 = await hc.get_text(path, params=base)
    obj1 = json.loads(text1)
    first = obj1.get("dados") or []
    dados_all: list[dict] = list(first if isinstance(first, list) else [])
    links1 = obj1.get("links") or []

    last_page = _extract_last_page(links1)
    has_next = _has_next(links1)

    # a) If there's a 'last' page number, do concurrent fan-out.
    if last_page > 1:
        pages = list(range(2, last_page + 1))

        async def worker(pg: int):
            t = await hc.get_text(path, params={**params, "pagina": pg, "itens": itens})
            o = json.loads(t)
            return pg, (o.get("dados") or [])

        results, _ = await bounded_gather_pbar(pages, worker, concurrency=concurrency)
        results.sort(key=lambda x: x[0])
        for _, rows in results:
            dados_all.extend(rows)
        return dados_all

    # b) If no 'last' but there's 'next', optionally walk sequentially.
    if has_next and fallback_follow_next:
        page = 2
        while True:
            t = await hc.get_text(path, params={**params, "pagina": page, "itens": itens})
            o = json.loads(t)
            rows = o.get("dados") or []
            if not rows:
                break
            dados_all.extend(rows)
            if not _has_next(o.get("links") or []):
                break
            page += 1

    return dados_all
