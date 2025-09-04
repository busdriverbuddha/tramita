# tramita/http/rate.py

import asyncio
import time


class RateLimiter:
    """
    Simple average rate limiter: ~rate_per_sec, 1 token per request.
    Deterministic enough for reproducible snapshots.
    """
    def __init__(self, rate_per_sec: float):
        self._interval = 1.0 / max(rate_per_sec, 0.0001)
        self._lock = asyncio.Lock()
        self._next = 0.0

    async def acquire(self):
        async with self._lock:
            now = time.monotonic()
            wait = max(0.0, self._next - now)
            self._next = (now + wait) + self._interval
        if wait:
            await asyncio.sleep(wait)
