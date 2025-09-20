# tramita/sources/senado/stages/blocos.py

import json
import logging
from collections import defaultdict
from typing import Iterable

import pyarrow.parquet as pq  # only used when reading previously written parts (optional)

from tramita.config import settings
from tramita.http.client import HttpClient
from tramita.log import setup_logging
from tramita.sources.senado.client import senado_fetch, _dig
from tramita.storage.manifest import SnapshotManifest
from tramita.storage.parquet import write_details_parts, write_relation_parts
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


async def build_blocos_details(
    paths: BronzePaths,
    manifest: SnapshotManifest,
    years: Iterable[int],
) -> int:
    """
    Fetch all blocos from /dados/ListaBlocoParlamentar.json and write Bronze details:
      - source="senado", entity="bloco"
      - id = CodigoBloco (numeric-as-string)
      - year = DataCriacao[:4] fallback to min(years)
      - url = SENADO_BASE + /dados/ListaBlocoParlamentar.json
      - payload_json = full bloco dict (deterministic JSON)
    Output: senado/bloco/details/year=YYYY/part-*.parquet
    """

    years_sorted = sorted(set(int(y) for y in years)) or [0]
    default_year = years_sorted[0]

    async with HttpClient(
        SENADO_BASE,
        rate_per_sec=settings.senado_rate,
        timeout=settings.http_timeout,
        user_agent=settings.user_agent,
    ) as hc:
        obj = await senado_fetch(hc, "/dados/ListaBlocoParlamentar.json", {})
        blocos = _dig(obj, ["ListaBlocoParlamentar", "Blocos", "Bloco"]) or []
        if not isinstance(blocos, list):
            log.warning("[senado:blocos] unexpected shape; no 'Bloco' list")
            return 0

        by_year: dict[int, list[dict]] = defaultdict(list)
        for b in blocos:
            bid = _safe_str_int(b.get("CodigoBloco"))
            if not bid:
                # extremely rare; keep a deterministic but skip if no primary id
                continue
            y = _year_of_str_date(b.get("DataCriacao"), default_year)
            pj = json.dumps(b, ensure_ascii=False, separators=(",", ":"), sort_keys=True)
            by_year[int(y)].append({
                "source": "senado",
                "entity": "bloco",
                "year": int(y),
                "id": bid,
                "url": f"{SENADO_BASE}/dados/ListaBlocoParlamentar.json",
                "payload_json": pj,
            })

        total_rows = 0
        for y, rows in sorted(by_year.items(), key=lambda kv: kv[0]):
            if not rows:
                continue
            parts = write_details_parts(
                rows,
                paths=paths,
                manifest=manifest,
                source="senado",
                entity="bloco",
                year=int(y),
                part_rows=50_000,
                sort=True,
            )
            total_rows += len(rows)
            log.info(f"[senado:blocos] year={y} wrote {len(rows)} rows in {len(parts)} part(s)")

    log.info(f"[senado:blocos] total rows={total_rows}")
    return total_rows


async def build_rel_bloco_partido(
    paths: BronzePaths,
    manifest: SnapshotManifest,
    years: Iterable[int],
) -> int:
    """
    Read previously written bloco details and emit one relation row per party membership:
      relation="bloco_partido"
      id = "<CodigoBloco>:<CodigoPartido>:<DataAdesao|'na'>"
      year = prefer DataAdesao[:4] -> DataCriacao[:4] -> default bucket
      url = SENADO_BASE + /dados/ListaBlocoParlamentar.json
      payload_json = original membership dict (with nested Partido,...)
    Output: senado/bloco_partido/year=YYYY/part-*.parquet
    """

    years_sorted = sorted(set(int(y) for y in years)) or []
    if not years_sorted:
        log.info("[senado:bloco_partido] no years requested; skipping")
        return 0

    total = 0

    by_year: dict[int, list[dict]] = defaultdict(list)

    # entity details root: .../senado/bloco/details
    probe_dir = paths.details_part_dir("senado", "bloco", (years_sorted or [0])[0]).parent
    if not probe_dir.exists():
        log.info(f"[senado:bloco_partido] no bloco details dir: {probe_dir}")
        return 0

    part_files = sorted(probe_dir.glob("year=*/part-*.parquet"))
    if not part_files:
        log.info(f"[senado:bloco_partido] no bloco detail parts under: {probe_dir}")
        return 0

    for pf in part_files:
        tbl = pq.read_table(pf, columns=["id", "payload_json"])
        for r in tbl.to_pylist():
            bid = str(r["id"])
            try:
                b = json.loads(r["payload_json"])
            except Exception:
                continue

            bloco_year_fallback = _year_of_str_date(b.get("DataCriacao"), 0)
            membros = (((b.get("Membros") or {}).get("Membro")) or [])
            if isinstance(membros, dict):
                membros = [membros]

            for mem in membros:
                pj = json.dumps(mem, ensure_ascii=False, separators=(",", ":"), sort_keys=True)
                partido = mem.get("Partido") or {}
                pid = _safe_str_int(partido.get("CodigoPartido")) or "na"
                adesao = mem.get("DataAdesao")
                part_year = _year_of_str_date(adesao, bloco_year_fallback or (years_sorted[0] if years_sorted else 0))
                rid = f"{bid}:{pid}:{adesao or 'na'}"
                by_year[int(part_year)].append({
                    "source": "senado",
                    "entity": "bloco_partido",
                    "year": int(part_year),
                    "id": rid,
                    "url": f"{SENADO_BASE}/dados/ListaBlocoParlamentar.json",
                    "payload_json": pj,
                })

        # write one partition per membership year
        for part_year, rows in sorted(by_year.items(), key=lambda kv: kv[0]):
            if not rows:
                continue
            write_relation_parts(
                rows,
                paths=paths,
                manifest=manifest,
                source="senado",
                relation="bloco_partido",
                year=int(part_year),
                part_rows=50_000,
                sort=True,
            )
            total += len(rows)
            log.info(f"[senado:bloco_partido] wrote {len(rows)} rows -> year={part_year}")

    log.info(f"[senado:bloco_partido] total rows={total}")
    return total
