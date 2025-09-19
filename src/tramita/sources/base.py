# tramita/sources/base.py

import asyncio
import json

from dataclasses import dataclass

from typing import Any, AsyncIterator, Callable, Iterable, TypeVar, Awaitable


from tramita.http.client import HttpClient


@dataclass
class FetchError:
    id: str
    url: str
    status: int | None
    message: str


T = TypeVar("T")  # item type
R = TypeVar("R")  # result type


async def bounded_gather(
    items: Iterable[Any],
    worker: Callable[[T], Awaitable[R]],
    concurrency: int = 20,
    on_progress: Callable[[int, int], None] | None = None,  # NEW (optional)
) -> tuple[list[Any], list[Exception]]:
    sem = asyncio.Semaphore(concurrency)
    results: list[Any] = []
    errors: list[Exception] = []

    items_list = list(items)  # we already create a task per item anyway
    total = len(items_list)
    done = 0

    async def run_one(x):
        async with sem:
            return await worker(x)

    tasks: list[asyncio.Task[R]] = [asyncio.create_task(run_one(x)) for x in items_list]
    for t in asyncio.as_completed(tasks):
        try:
            results.append(await t)
        except Exception as e:
            errors.append(e)
        finally:
            done += 1
            if on_progress:
                on_progress(done, total)
    return results, errors


async def paginate_json(
    client: HttpClient,
    path: str,
    params: dict[str, Any],
    *,
    page_param: str = "pagina",
    page_start: int = 1,
    page_size_param: str | None = None,
    page_size_value: int | None = None,
    data_key: str = "dados",
    next_in_links: bool = True,
) -> AsyncIterator[list[dict]]:
    """
    Câmara defaults: ?pagina=1&itens=100; response has {"dados":[...], "links":[...]}
    This yields each page's 'dados' as a list of dicts until no next page is found.
    """
    page = page_start
    params = dict(params)
    if page_size_param and page_size_value:
        params[page_size_param] = page_size_value

    while True:
        params[page_param] = page
        text = await client.get_text(path, params=params)
        obj = json.loads(text)
        rows = obj.get(data_key) or []
        yield rows
        if not rows:
            break
        if next_in_links:
            has_next = any(link.get("rel") == "next" for link in obj.get("links", []))
            if not has_next:
                break
        else:
            # if API doesn't give links, stop when rows < page_size
            if page_size_value and len(rows) < page_size_value:
                break
        page += 1


async def bounded_gather_pbar(
    items: Iterable[Any],
    worker: Callable[[T], Awaitable[R]],
    *,
    concurrency: int = 20,
    description: str = "requests",
) -> tuple[list[Any], list[Exception]]:
    from tramita.ui import progress_reporter
    items_list = list(items)
    with progress_reporter(len(items_list), description) as on_progress:
        return await bounded_gather(items_list, worker, concurrency=concurrency, on_progress=on_progress)
