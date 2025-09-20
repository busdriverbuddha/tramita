# tramita/sources/senado/stages/partidos.py

import json
import logging
from collections import defaultdict
from typing import Iterable

from tramita.config import settings
from tramita.http.client import HttpClient
from tramita.log import setup_logging
from tramita.sources.senado.client import senado_fetch, _dig
from tramita.storage.manifest import SnapshotManifest
from tramita.storage.parquet import write_details_parts
from tramita.storage.paths import BronzePaths

setup_logging()
log = logging.getLogger(__name__)

SENADO_BASE = settings.senado_base_url.rstrip("/")


def _safe_str_int(x) -> str | None:
    if x is None:
        return None
    try:
        return str(int(x))
    except Exception:
        return str(x)


def _year_of_str_date(s: str | None, default_year: int) -> int:
    if isinstance(s, str) and len(s) >= 4 and s[:4].isdigit():
        try:
            return int(s[:4])
        except Exception:
            pass
    return int(default_year)


async def build_partidos_details(
    paths: BronzePaths,
    manifest: SnapshotManifest,
    years: Iterable[int],
) -> int:
    """
    Fetch all partidos from /dados/ListaPartidos.json and write Bronze details:
      - source="senado", entity="partido"
      - id = Codigo (numeric-as-string)
      - year = DataCriacao[:4] fallback to min(years)
      - url = SENADO_BASE + /dados/ListaPartidos.json
      - payload_json = full partido dict
    Output: senado/partido/details/year=YYYY/part-*.parquet
    """

    years_sorted = sorted(set(int(y) for y in years)) or [0]
    default_year = years_sorted[0]

    async with HttpClient(
        SENADO_BASE,
        rate_per_sec=settings.senado_rate,
        timeout=settings.http_timeout,
        user_agent=settings.user_agent,
    ) as hc:
        obj = await senado_fetch(hc, "/dados/ListaPartidos.json", {})
        plist = _dig(obj, ["ListaPartidos", "Partidos", "Partido"]) or []
        if not isinstance(plist, list):
            log.warning("[senado:partidos] unexpected shape; no 'Partido' list")
            return 0

        by_year: dict[int, list[dict]] = defaultdict(list)
        for p in plist:
            pid = _safe_str_int(p.get("Codigo"))
            if not pid:
                continue
            y = _year_of_str_date(p.get("DataCriacao"), default_year)
            pj = json.dumps(p, ensure_ascii=False, separators=(",", ":"), sort_keys=True)
            by_year[int(y)].append({
                "source": "senado",
                "entity": "partido",
                "year": int(y),
                "id": pid,
                "url": f"{SENADO_BASE}/dados/ListaPartidos.json",
                "payload_json": pj,
            })

        total = 0
        for y, rows in sorted(by_year.items(), key=lambda kv: kv[0]):
            if not rows:
                continue
            parts = write_details_parts(
                rows,
                paths=paths,
                manifest=manifest,
                source="senado",
                entity="partido",
                year=int(y),
                part_rows=50_000,
                sort=True,
            )
            total += len(rows)
            log.info(f"[senado:partidos] year={y} wrote {len(rows)} rows in {len(parts)} part(s)")

    log.info(f"[senado:partidos] total rows={total}")
    return total
