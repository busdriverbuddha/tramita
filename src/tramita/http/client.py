# src/tramita/http/client.py

import hashlib
import httpx

from typing import Optional

from tramita.http.backoff import async_retry
from tramita.http.rate import RateLimiter


class HttpError(Exception):
    def __init__(self, message: str, status_code: Optional[int] = None):
        super().__init__(message)
        self.status_code = status_code


class HttpClient:
    def __init__(self, base_url: str, *, rate_per_sec: float, timeout: float, user_agent: str):
        self._rate = RateLimiter(rate_per_sec)
        self._client = httpx.AsyncClient(
            base_url=base_url.rstrip("/"),
            timeout=timeout,
            headers={"Accept-Encoding": "gzip", "User-Agent": user_agent},
            http2=True,
        )
        self._closed = False

    async def aclose(self):
        if not self._closed:
            await self._client.aclose()
            self._closed = True

    async def __aenter__(self):
        return self

    async def __aexit__(self, *exc):
        await self.aclose()

    @async_retry()
    async def get_text(self, path_or_url: str, params: Optional[dict] = None) -> str:
        # Rate-limit *before* the request to reduce server load deterministically
        await self._rate.acquire()
        try:
            r = await self._client.get(path_or_url, params=params)
        except httpx.HTTPError as e:
            raise HttpError(f"HTTP transport error: {e}") from e
        if r.status_code >= 400:
            err = HttpError(f"HTTP {r.status_code} for {r.url}", status_code=r.status_code)
            raise err
        return r.text

    @staticmethod
    def sha256(text: str) -> str:
        return hashlib.sha256(text.encode("utf-8")).hexdigest()
