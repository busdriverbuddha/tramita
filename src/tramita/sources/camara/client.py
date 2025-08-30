# tramita/sources/camara/client.py

import json
import re

from typing import Any

from tramita.sources.base import bounded_gather
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


async def camara_fetch_all_dados(
    hc: HttpClient,
    path: str,
    params: dict[str, Any],
    *,
    itens: int = 100,
    concurrency: int = 8,
    fallback_follow_next: bool = True,
) -> list[dict]:
    """
    Fetches all pages using the 'last' link trick. Returns concatenated 'dados' in page order.
    If 'last' is missing and fallback is True, follows next pages sequentially.
    """
    # 1) first page
    base = dict(params)
    base.update({"pagina": 1, "itens": itens})
    text1 = await hc.get_text(path, params=base)
    obj1 = json.loads(text1)
    dados_all: list[dict] = list(obj1.get("dados") or [])
    links1: list[dict] = obj1.get("links") or []

    last_page = _extract_last_page(links1)

    # 2) fast path if only one page
    if last_page <= 1:
        # optional fallback if there was a 'next' but no 'last'
        has_next = any((link.get("rel") or "").lower() == "next" for link in links1)
        if not (fallback_follow_next and has_next):
            return dados_all

        # fallback: walk pagina=2,3,... until empty/stop
        page = 2
        while True:
            t = await hc.get_text(path, params=base | {"pagina": page})
            o = json.loads(t)
            rows = o.get("dados") or []
            if not rows:
                break
            dados_all.extend(rows)
            # stop if links say no next
            links = o.get("links") or []
            has_next = any((link.get("rel") or "").lower() == "next" for link in links)
            if not has_next:
                break
            page += 1
        return dados_all

    # 3) fetch remaining pages concurrently
    pages = list(range(2, last_page + 1))

    async def worker(pg: int):
        t = await hc.get_text(path, params=base | {"pagina": pg})
        o = json.loads(t)
        return pg, (o.get("dados") or [])

    results, errs = await bounded_gather(pages, worker, concurrency=concurrency)
    # determinism: sort by page number regardless of completion order
    results.sort(key=lambda x: x[0])
    for _, rows in results:
        dados_all.extend(rows)
    return dados_all