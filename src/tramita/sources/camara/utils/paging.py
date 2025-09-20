# tramita/sources/camara/utils/paging.py

import hashlib

from datetime import date, timedelta


def _iter_date_windows(start: date, end: date, *, days: int) -> list[tuple[date, date]]:
    """Left-closed, right-closed windows: [d0, d1]."""
    out: list[tuple[date, date]] = []
    d = start
    while d <= end:
        d1 = min(d + timedelta(days=days - 1), end)
        out.append((d, d1))
        d = d1 + timedelta(days=1)
    return out


def _parse_fraction(spec: str | None) -> tuple[int | None, int | None]:
    # spec like "1/200" => (1, 200)
    if not spec:
        return None, None
    a, b = spec.split("/", 1)
    return int(a), int(b)


def _hash_take(pid: str, keep_num: int | None, keep_den: int | None) -> bool:
    if not keep_num or not keep_den:
        return True
    h = hashlib.sha256(pid.encode("utf-8")).hexdigest()
    val = int(h[:8], 16)  # 32-bit slice is enough
    return (val % keep_den) < keep_num
