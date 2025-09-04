# tramita/http/backoff.py

import asyncio
import random

from typing import Callable


RETRY_STATUSES = {429, 500, 502, 503, 504}


def should_retry(status: int) -> bool:
    return status in RETRY_STATUSES


def async_retry(max_attempts: int = 6, base: float = 0.5, cap: float = 8.0):
    def deco(fn: Callable):
        async def inner(*args, **kwargs):
            attempt = 1
            while True:
                try:
                    return await fn(*args, **kwargs)
                except Exception as e:
                    # Allow wrapped functions to pass (status, transient) via e.args
                    status = getattr(e, "status_code", None)
                    if attempt >= max_attempts or (status is not None and not should_retry(status)):
                        raise
                    sleep = min(cap, base * (2 ** (attempt - 1)))
                    sleep *= 1 + random.random() * 0.25  # jitter
                    await asyncio.sleep(sleep)
                    attempt += 1
        return inner
    return deco
