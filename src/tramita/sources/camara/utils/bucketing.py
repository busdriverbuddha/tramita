# tramita/sources/camara/utils/bucketing.py

import re

from typing import Any, Iterable


_DATE_RE = re.compile(r"\d{4}-\d{2}-\d{2}")


def _collect_years_from_obj(o: Any, acc: set[int] | None = None) -> set[int]:
    """
    Best-effort: walk lists/dicts/strings and collect YYYY from ISO-like dates.
    Keeps Bronze "raw" while giving us a deterministic year bucket when possible.
    """
    if acc is None:
        acc = set()
    if isinstance(o, dict):
        for k, v in o.items():
            # keys often like dataInicio, dataFim, dataHora, etc.
            if isinstance(v, str):
                for m in _DATE_RE.finditer(v):
                    try:
                        acc.add(int(m.group(0)[:4]))
                    except Exception:
                        pass
            _collect_years_from_obj(v, acc)
    elif isinstance(o, list):
        for it in o:
            _collect_years_from_obj(it, acc)
    elif isinstance(o, str):
        for m in _DATE_RE.finditer(o):
            try:
                acc.add(int(m.group(0)[:4]))
            except Exception:
                pass
    return acc


def _bucket_year_for_items(items: list[dict], years: Iterable[int], default_bucket: int) -> int:
    """
    Pick a deterministic year bucket:
      1) if any 'date-like' years inside items fall within [min(years), max(years)], pick the earliest
      2) else if any years found, pick the earliest overall
      3) else fallback to default_bucket
    """
    yr_set = _collect_years_from_obj(items or [])
    if not yr_set:
        return default_bucket
    y0, y1 = min(years), max(years)
    in_range = sorted(y for y in yr_set if y0 <= y <= y1)
    if in_range:
        return in_range[0]
    return min(yr_set)
