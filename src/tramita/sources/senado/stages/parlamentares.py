# tramita/sources/senado/stages/parlamentares.py

import json
import logging
import pyarrow.parquet as pq
from datetime import date

from typing import Any, Iterable

from tramita.config import settings
from tramita.http.client import HttpClient
from tramita.log import setup_logging
from tramita.sources.base import bounded_gather_pbar
from tramita.sources.senado.client import senado_fetch, _dig
from tramita.storage.manifest import SnapshotManifest
from tramita.storage.parquet import write_index_parquet, write_details_parts
from tramita.storage.paths import BronzePaths
from tramita.sources.senado.utils import _year_hits_legislatura

setup_logging()
log = logging.getLogger(__name__)

SENADO_BASE = settings.senado_base_url.rstrip("/")


async def build_index_parlamentares_via_autoria(
    paths: BronzePaths,
    years: Iterable[int],
) -> int:
    """
    Build a per-year index of unique senators (codigoParlamentar) referenced in processo details.

    Reads:  senado/processo/details/year=YYYY/part-*.parquet
    Writes: senado/parlamentar/index/year=YYYY/ids.parquet
      - id   = codigoParlamentar (string)
      - url  = f"{SENADO_BASE}/parlamentar/{codigoParlamentar}"
    """
    import json
    from collections import defaultdict
    from pathlib import Path
    import pyarrow.parquet as pq

    setup_logging()
    log = logging.getLogger(__name__)

    def _norm_code(x) -> str | None:
        if x is None:
            return None
        try:
            return str(int(x))
        except Exception:
            return str(x)

    def _year_of(obj: dict, default_year: int) -> int:
        doc = obj.get("documento") or {}
        da = doc.get("dataApresentacao") or doc.get("data")
        if isinstance(da, str) and len(da) >= 4 and da[:4].isdigit():
            try:
                return int(da[:4])
            except Exception:
                pass
        ano = obj.get("ano")
        try:
            return int(ano) if ano is not None else int(default_year)
        except Exception:
            return int(default_year)

    # year -> set of senator codes
    per_year_codes: dict[int, set[str]] = defaultdict(set)
    total_codes = 0

    for y in sorted(set(years)):
        details_dir = paths.details_part_dir("senado", "processo", y)
        if not details_dir.exists():
            log.warning(f"[senado:parlamentar_idx] missing details dir for year={y}: {details_dir}")
            continue

        parts = sorted(Path(details_dir).glob("part-*.parquet"))
        if not parts:
            log.warning(f"[senado:parlamentar_idx] no parts for year={y}: {details_dir}")
            continue

        for pf in parts:
            table = pq.read_table(pf, columns=["payload_json"])
            for row in table.to_pylist():
                try:
                    obj = json.loads(row["payload_json"])
                except Exception:
                    continue

                # Pull from documento.autoria and autoriaIniciativa
                codes: set[str] = set()
                for coll in [(obj.get("documento") or {}).get("autoria") or [], obj.get("autoriaIniciativa") or []]:
                    for a in coll:
                        cp = _norm_code(a.get("codigoParlamentar"))
                        if cp:  # senator authors only
                            codes.add(cp)

                if not codes:
                    continue

                part_year = _year_of(obj, y)
                for cp in codes:
                    if cp not in per_year_codes[part_year]:
                        per_year_codes[part_year].add(cp)
                        total_codes += 1

    # write per-year index
    total_written = 0
    for year_bucket, codes in sorted(per_year_codes.items(), key=lambda kv: kv[0]):
        rows = [{
            "source": "senado",
            "entity": "parlamentar",
            "year": int(year_bucket),
            "id": cp,
            "url": f"{SENADO_BASE}/parlamentar/{cp}",
        } for cp in sorted(codes, key=lambda s: s.zfill(6))]

        if not rows:
            continue

        out = paths.index_file("senado", "parlamentar", int(year_bucket))
        n = write_index_parquet(rows, out)
        total_written += n
        log.info(f"[senado:parlamentar_idx] year={year_bucket} wrote {n} senator ids -> {out}")

    log.info(f"[senado:parlamentar_idx] unique ids written={total_written} (from {total_codes} discoveries)")
    return total_written


async def build_index_parlamentares_via_legislaturas(
    paths: BronzePaths,
    years: Iterable[int],
) -> int:
    """
    Variante baseada em legislaturas que escreve senado/parlamentar/index/year=YYYY/ids.parquet
    (id = CodigoParlamentar; url = /parlamentar/{id})
    """
    from tramita.config import settings

    codes_by_year = await _parlamentares_codes_by_year_via_legislaturas(years)
    total = 0
    SENADO_BASE = settings.senado_base_url.rstrip("/")

    for y, codes in sorted(codes_by_year.items()):
        if not codes:
            continue
        rows = [{
            "source": "senado",
            "entity": "parlamentar",
            "year": int(y),
            "id": c,
            "url": f"{SENADO_BASE}/parlamentar/{c}",
        } for c in sorted(codes, key=lambda s: s.zfill(6))]
        n = write_index_parquet(rows, paths.index_file("senado", "parlamentar", int(y)))
        total += n
    return total


async def build_details_parlamentares(
    paths: BronzePaths,
    manifest: SnapshotManifest,
    year: int,
    *,
    concurrency: int = 12,
) -> int:
    """
    Read senado/parlamentar/index/year=YYYY and fetch details from /senador/{id}.json.
    """

    idx = paths.index_file("senado", "parlamentar", year)
    if not idx.exists():
        log.warning(f"[senado:parlamentar_details] missing index for year={year}: {idx}")
        return 0

    table = pq.read_table(idx)
    ids: list[str] = sorted({str(r["id"]) for r in table.to_pylist()})
    if not ids:
        log.info(f"[senado:parlamentar_details] year={year} no ids")
        return 0

    async with HttpClient(
        SENADO_BASE,
        rate_per_sec=settings.senado_rate,
        timeout=settings.http_timeout,
        user_agent=settings.user_agent,
    ) as hc:
        async def worker(pid: str):
            # Endpoint format: /senador/{id}.json
            obj = await senado_fetch(hc, f"/senador/{pid}.json", {})
            payload_json = json.dumps(
                obj,
                ensure_ascii=False,
                separators=(",", ":"),  # deterministic
                sort_keys=True,
            )
            return {
                "source": "senado",
                "entity": "parlamentar",
                "year": year,
                "id": pid,
                "url": f"{SENADO_BASE}/senador/{pid}.json",
                "payload_json": payload_json,
            }

        rows, errs = await bounded_gather_pbar(
            ids, worker, concurrency=concurrency, description=f"senado:parlamentar_details:{year}"
        )
        if errs:
            log.warning(f"[senado:parlamentar_details] year={year} errors={len(errs)} (partial write)")

    parts = write_details_parts(
        rows,
        paths=paths,
        manifest=manifest,
        source="senado",
        entity="parlamentar",
        year=year,
        part_rows=50_000,
        sort=True,
    )
    log.info(f"[senado:parlamentar_details] year={year} wrote {len(rows)} rows in {len(parts)} part(s)")
    return len(rows)


async def _parlamentares_codes_by_year_via_legislaturas(
    years: Iterable[int],
) -> dict[int, set[str]]:
    """
    Retorna um dicionário {ano -> {CodigoParlamentar}} em RAM, unindo
    todas as legislaturas que cobrem cada ano.
    """
    from tramita.config import settings

    years_sorted = sorted(set(int(y) for y in years))
    out: dict[int, set[str]] = {y: set() for y in years_sorted}

    async with HttpClient(
        settings.senado_base_url,
        rate_per_sec=settings.senado_rate,
        timeout=settings.http_timeout,
        user_agent=settings.user_agent,
    ) as hc:
        leg_nums, bounds = await _resolve_legislaturas_for_years(hc, years_sorted)
        if not leg_nums:
            return out

        async def worker(n: int) -> tuple[int, set[str]]:
            return await _fetch_parlamentares_codes_for_legislatura(hc, n)

        results, errs = await bounded_gather_pbar(
            leg_nums,
            worker,
            concurrency=8,
            description="senado:leg->parlamentares",
        )
        if errs:
            log.warning(f"[senado:parlamentares] {len(errs)} erro(s) ao buscar legislaturas")

        # leg -> {codes}
        leg_to_codes: dict[int, set[str]] = {leg: codes for (leg, codes) in results}

        # espalha por ano: ano recebe a união dos códigos das legislaturas que o cobrem
        for y in years_sorted:
            for leg, codes in leg_to_codes.items():
                ini, fim = bounds.get(leg, (date.min, date.min))
                if _year_hits_legislatura(y, ini, fim):
                    out[y].update(codes)

    return out


async def _fetch_parlamentares_codes_for_legislatura(
    hc: HttpClient,
    numero_leg: int,
) -> tuple[int, set[str]]:
    """
    Baixa /senador/lista/legislatura/{N}.json e retorna (N, {codigos}).
    """
    path = f"/senador/lista/legislatura/{numero_leg}.json"
    obj = await senado_fetch(hc, path, {})
    plist = _dig(obj, ["ListaParlamentarLegislatura", "Parlamentares", "Parlamentar"]) or []
    codes: set[str] = set()
    for p in plist:
        raw = None
        try:
            raw = ((p.get("IdentificacaoParlamentar") or {}).get("CodigoParlamentar"))
            if raw is None:
                continue
            codes.add(str(int(raw)))
        except Exception:
            if raw is not None:
                codes.add(str(raw))
    return numero_leg, codes


async def _resolve_legislaturas_for_years(
    hc: HttpClient,
    years: Iterable[int],
) -> tuple[list[int], dict[int, tuple[date, date]]]:
    """
    Lê /dados/ListaLegislatura.json e retorna:
      - lista ordenada dos números de legislatura que intersectam os anos pedidos
      - mapa num_legislatura -> (data_inicio, data_fim)
    """
    obj = await senado_fetch(hc, "/dados/ListaLegislatura.json", {})
    legs: list[dict[str, Any]] = _dig(obj, ["ListaLegislatura", "Legislaturas", "Legislatura"]) or []

    selected: set[int] = set()
    bounds: dict[int, tuple[date, date]] = {}

    ys = sorted(set(int(y) for y in years))
    for leg in legs:
        try:
            n = int(leg["NumeroLegislatura"])
            ini = date.fromisoformat(leg["DataInicio"])
            fim = date.fromisoformat(leg["DataFim"])
        except Exception:
            continue
        bounds[n] = (ini, fim)
        if any(_year_hits_legislatura(y, ini, fim) for y in ys):
            selected.add(n)

    return sorted(selected), bounds
