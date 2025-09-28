# tramita/sources/senado/stages/processos.py

import hashlib
import json
import logging

from collections import defaultdict
from datetime import date, timedelta
from typing import Any, Iterable

import pyarrow.parquet as pq

from tramita.config import settings
from tramita.http.client import HttpClient
from tramita.log import setup_logging
from tramita.sources.base import bounded_gather_pbar
from tramita.sources.senado.client import senado_fetch, senado_fetch_list
from tramita.sources.senado.utils import _first_present
from tramita.storage.manifest import SnapshotManifest
from tramita.storage.parquet import write_index_parquet, write_details_parts, write_relation_parts
from tramita.storage.paths import BronzePaths

setup_logging()
log = logging.getLogger(__name__)

SENADO_BASE = settings.senado_base_url.rstrip("/")


async def build_index_processos(
    paths: BronzePaths,
    years: Iterable[int],
    window_days: int = 30,
    *,
    # leave type filter param name flexible until confirmed (siglaMateria? tipo?):
    tipo_siglas: list[str] | None = None,
) -> int:
    """
    Build Senado matérias index using date windows within each requested year.
    For each year y ∈ years, iterate windows from y-01-01 to y-12-31, with:
      - dataInicioDeliberacao = window start (YYYY-MM-DD)
      - dataFimDeliberacao   = window end   (YYYY-MM-DD)
    NOTE: We DO NOT send 'ano' as a query parameter.
    Bucketing = the year being iterated (deterministic).
    """
    total = 0

    years_sorted = sorted(set(years))

    async with HttpClient(
        SENADO_BASE,
        rate_per_sec=settings.senado_rate,
        timeout=settings.http_timeout,
        user_agent=settings.user_agent,
    ) as hc:
        for y in years_sorted:
            year_start = date(y, 1, 1)
            year_end = date(y, 12, 31)

            # Collect unique IDs for the whole year to avoid counting duplicates across windows.
            unique_ids_for_year: set[str] = set()

            cur = year_start
            while cur <= year_end:
                win_end = min(cur + timedelta(days=window_days - 1), year_end)

                params: dict[str, Any] = {
                    "dataInicioDeliberacao": cur.isoformat(),
                    "dataFimDeliberacao": win_end.isoformat(),
                }
                if tipo_siglas:
                    # The API tolerates unknowns; keeping 'sigla' until we confirm the exact field.
                    params["sigla"] = ",".join(tipo_siglas)

                dados = await senado_fetch_list(
                    hc, "/processo", params,
                    candidates=None,  # use defaults in client
                )

                for it in dados or []:
                    mid = _first_present(
                        it,
                        ("id",),
                    )
                    if mid:
                        unique_ids_for_year.add(mid)

                # next window
                cur = win_end + timedelta(days=1)

            # Write once per year with de-duplicated IDs
            if unique_ids_for_year:
                rows = [{
                    "source": "senado",
                    "entity": "processo",
                    "year": y,
                    "id": mid,
                    "url": f"{SENADO_BASE}/processo/{mid}",
                } for mid in sorted(unique_ids_for_year)]

                n = write_index_parquet(rows, paths.index_file("senado", "processo", y))
                total += n
                log.info(f"[senado:index] year={y} windows dedup={n}")

    log.info(f"[senado:index] total={total}")
    return total


async def build_details_processos(  # kept name/signature for drop-in use
    paths: BronzePaths,
    manifest: SnapshotManifest,
    years: Iterable[int],
    *,
    concurrency: int = 16,
    max_rounds: int = 8,  # ignored
) -> int:
    """
    Fetch /processo/{id} details *only* for IDs present in
    senado/processo/index/year=YYYY/ids.parquet (no related expansion).

    Each fetched detail is bucketed by its natural year:
      - prefer field 'ano'
      - fallback: documento.dataApresentacao[:4]
      - last resort: the smallest requested year

    Details are written to senado/processo/details/year=YYYY/part-*.parquet
    and recorded into the manifest.

    Returns total number of unique processos fetched.
    """

    years_sorted = sorted({int(y) for y in years})
    if not years_sorted:
        return 0

    # ---- Seed set of IDs from existing per-year index files
    seed_ids: set[str] = set()
    for y in years_sorted:
        idx_path = paths.index_file("senado", "processo", y)
        if idx_path.exists():
            tbl = pq.read_table(idx_path, columns=["id"])
            # tbl.to_pylist() gives list[dict]; cast IDs to str to normalize
            seed_ids.update(str(r["id"]) for r in tbl.to_pylist())

    if not seed_ids:
        log.info("[senado:proc_details] no ids found in index; nothing to do")
        return 0

    # ---- Helpers
    def _infer_year(obj: dict) -> int:
        ano = obj.get("ano")
        if ano is not None:
            try:
                return int(ano)
            except Exception:
                pass
        try:
            da = ((obj.get("documento") or {}).get("dataApresentacao"))
            if isinstance(da, str) and len(da) >= 4 and da[:4].isdigit():
                return int(da[:4])
        except Exception:
            pass
        return years_sorted[0]

    async with HttpClient(
        SENADO_BASE,
        rate_per_sec=settings.senado_rate,
        timeout=settings.http_timeout,
        user_agent=settings.user_agent,
    ) as hc:

        async def worker(pid: str):
            obj = await senado_fetch(hc, f"/processo/{pid}", {})
            year = _infer_year(obj)
            payload_json = json.dumps(
                obj,
                ensure_ascii=False,
                separators=(",", ":"),
                sort_keys=True,
            )
            return int(year), {
                "source": "senado",
                "entity": "processo",
                "year": int(year),
                "id": pid,
                "url": f"{SENADO_BASE}/processo/{pid}",
                "payload_json": payload_json,
            }

        batch = sorted(seed_ids)
        log.info(f"[senado:proc_details] fetching {len(batch)} ids (no expansion)")

        pairs, errs = await bounded_gather_pbar(
            batch, worker, concurrency=concurrency,
            description="senado:proc_details"
        )
        if errs:
            log.warning(f"[senado:proc_details] errors={len(errs)} (continuing)")

    # ---- Group by year and write parts deterministically
    by_year_rows: dict[int, list[dict]] = defaultdict(list)
    for year, row in pairs:
        by_year_rows[int(year)].append(row)

    total_written = 0
    for year, rows in sorted(by_year_rows.items(), key=lambda kv: kv[0]):
        if not rows:
            continue
        parts = write_details_parts(
            rows,
            paths=paths,
            manifest=manifest,
            source="senado",
            entity="processo",
            year=int(year),
            part_rows=50_000,
            sort=True,
        )
        total_written += len(rows)
        log.info(
            f"[senado:proc_details] year={year} wrote {len(rows)} rows "
            f"in {len(parts)} part(s)"
        )

    log.info(f"[senado:proc_details] DONE total unique detalhes={total_written}")
    return total_written


# build_votacoes_relations_senado

async def build_votacoes_relations(
    paths: BronzePaths,
    manifest: SnapshotManifest,
    years: Iterable[int],
    *,
    concurrency_processos: int = 12,
) -> int:
    """
    For each indexed processo in the given years, hit /votacao?idProcesso=<id>
    and write one Bronze 'votacoes' row per voting session returned.

    Rows are partitioned by the voting session year (from dataSessao or ano).
    """

    def _rid(v: dict) -> str:
        pid = str(v.get("idProcesso") or "")
        csv = v.get("codigoSessaoVotacao")
        if csv is not None:
            try:
                return f"{pid}:{int(csv)}"
            except Exception:
                return f"{pid}:{csv}"
        cs = v.get("codigoSessao")
        seq = v.get("sequencialSessao")
        if cs is not None and seq is not None:
            try:
                return f"{pid}:{int(cs)}:{int(seq)}"
            except Exception:
                return f"{pid}:{cs}:{seq}"
        # deterministic fallback
        pj = json.dumps(v, ensure_ascii=False, separators=(",", ":"), sort_keys=True)
        return f"{pid}:{hashlib.sha256(pj.encode('utf-8')).hexdigest()[:16]}"

    def _year_of(v: dict) -> int:
        ds = v.get("dataSessao")
        if isinstance(ds, str) and len(ds) >= 4 and ds[:4].isdigit():
            return int(ds[:4])
        ano = v.get("ano")
        if isinstance(ano, int):
            return ano
        try:
            return int(str(ano))
        except Exception:
            # very rare; last resort—keep inside the requested year bucket 0 to avoid misfile
            return 0

    total_rows = 0
    years_sorted = sorted(set(years))

    async with HttpClient(
        SENADO_BASE,
        rate_per_sec=settings.senado_rate,
        timeout=settings.http_timeout,
        user_agent=settings.user_agent,
    ) as hc:
        for y in years_sorted:
            idx_path = paths.index_file("senado", "processo", y)
            if not idx_path.exists():
                log.warning(f"[senado:votacoes] missing index for year={y}: {idx_path}")
                continue

            table = pq.read_table(idx_path)
            pids: list[str] = sorted({str(r["id"]) for r in table.to_pylist()})
            if not pids:
                continue

            async def worker(pid: str) -> list[dict]:
                items = await senado_fetch_list(hc, "/votacao", {"idProcesso": pid}, candidates=[["_list"]])
                rows: list[dict] = []
                for v in items or []:
                    payload_json = json.dumps(v, ensure_ascii=False, separators=(",", ":"), sort_keys=True)
                    rows.append({
                        "source": "senado",
                        "entity": "votacoes",
                        "year": _year_of(v),
                        "id": _rid(v),
                        "url": f"{SENADO_BASE}/votacao?idProcesso={pid}",
                        "payload_json": payload_json,
                    })
                return rows

            lists, errs = await bounded_gather_pbar(pids, worker, concurrency=concurrency_processos,
                                                    description=f"senado:votacoes:{y}")
            if errs:
                log.warning(f"[senado:votacoes] year={y} errors={len(errs)} (partial write)")

            # flatten & group by session year
            all_rows: list[dict] = [r for lst in lists for r in lst]
            by_year: dict[int, list[dict]] = defaultdict(list)
            for r in all_rows:
                by_year[int(r["year"])].append(r)

            # write each partition year separately
            for part_year, rows in sorted(by_year.items(), key=lambda kv: kv[0]):
                if part_year == 0:
                    # extremely rare; put under a neutral bucket to avoid IO errors
                    part_year = y
                    for r in rows:
                        r["year"] = part_year
                write_relation_parts(
                    rows,
                    paths=paths,
                    manifest=manifest,
                    source="senado",
                    relation="votacoes",
                    year=part_year,
                    part_rows=50_000,
                    sort=True,
                )
                total_rows += len(rows)
                log.info(f"[senado:votacoes] wrote {len(rows)} rows into year={part_year}")

    log.info(f"[senado:votacoes] total rows={total_rows}")
    return total_rows

# build_emendas_relations_senado


async def build_emendas_relations(
    paths: BronzePaths,
    manifest: SnapshotManifest,
    years: Iterable[int],
    *,
    concurrency_processos: int = 12,
) -> int:
    """
    For each indexed processo, hit /processo/emenda?idProcesso=<id>
    and write one Bronze 'emendas' row per amendment returned.

    Partition year: prefer dataApresentacao[:4]; fallback to the index bucket year.
    Row id: "<idProcesso>:<idEmenda>" for stability.
    """

    total_rows = 0
    years_sorted = sorted(set(int(y) for y in years))

    def _row_id(pid: str, emenda: dict) -> str:
        # emenda['id'] tends to be globally unique, but we prefix with processo for extra safety
        eid = emenda.get("id")
        try:
            eid_s = str(int(eid)) if eid is not None else "na"
        except Exception:
            eid_s = str(eid)
        return f"{pid}:{eid_s}"

    def _year_of(emenda: dict, default_year: int) -> int:
        ds = emenda.get("dataApresentacao")
        if isinstance(ds, str) and len(ds) >= 4 and ds[:4].isdigit():
            try:
                return int(ds[:4])
            except Exception:
                pass
        return int(default_year)

    async with HttpClient(
        SENADO_BASE,
        rate_per_sec=settings.senado_rate,
        timeout=settings.http_timeout,
        user_agent=settings.user_agent,
    ) as hc:
        for y in years_sorted:
            idx_path = paths.index_file("senado", "processo", y)
            if not idx_path.exists():
                log.warning(f"[senado:emendas] missing index for year={y}: {idx_path}")
                continue

            table = pq.read_table(idx_path, columns=["id"])
            pids: list[str] = sorted({str(r["id"]) for r in table.to_pylist()})
            if not pids:
                continue

            async def worker(pid: str) -> list[dict]:
                items = await senado_fetch_list(
                    hc, "/processo/emenda", {"idProcesso": pid},
                    candidates=[["_list"], ["resultados"], ["Itens"]]  # liberal, like other callers
                )
                rows: list[dict] = []
                if not items:
                    return rows
                for em in items:
                    payload_json = json.dumps(em, ensure_ascii=False, separators=(",", ":"), sort_keys=True)
                    rows.append({
                        "source": "senado",
                        "entity": "emendas",
                        "year": _year_of(em, y),
                        "id": _row_id(pid, em),
                        "url": f"{SENADO_BASE}/processo/emenda?idProcesso={pid}",
                        "payload_json": payload_json,
                    })
                return rows

            lists, errs = await bounded_gather_pbar(
                pids, worker, concurrency=concurrency_processos, description=f"senado:emendas:{y}"
            )
            if errs:
                log.warning(f"[senado:emendas] year={y} errors={len(errs)} (partial write)")

            # flatten & group by partition year
            all_rows: list[dict] = [r for lst in lists for r in lst]
            by_year: dict[int, list[dict]] = defaultdict(list)
            for r in all_rows:
                by_year[int(r["year"])].append(r)

            for part_year, rows in sorted(by_year.items(), key=lambda kv: kv[0]):
                if not rows:
                    continue
                # very rare: guard against year=0 etc.
                if part_year <= 0:
                    part_year = y
                    for r in rows:
                        r["year"] = part_year
                write_relation_parts(
                    rows,
                    paths=paths,
                    manifest=manifest,
                    source="senado",
                    relation="emendas",
                    year=int(part_year),
                    part_rows=50_000,
                    sort=True,
                )
                total_rows += len(rows)
                log.info(f"[senado:emendas] wrote {len(rows)} rows into year={part_year}")

    log.info(f"[senado:emendas] total rows={total_rows}")
    return total_rows


async def build_relatorias_relations(
    paths: BronzePaths,
    manifest: SnapshotManifest,
    years: Iterable[int],
    *,
    concurrency_processos: int = 12,
) -> int:
    """
    For each indexed processo, hit /processo/relatoria?idProcesso=<id>
    and write one Bronze 'relatorias' row per item returned.

    Partition year: prefer dataDesignacao[:4];
      fallback to dataDestituicao[:4];
      fallback to dataApresentacaoProcesso[:4];
      fallback to the index bucket year.

    Row id: prefer relatoria['id'] (stable); else a deterministic composite:
      "<idProcesso>:<idTipoRelator>:<dataDesignacao>:<codigoParlamentar>"
    """

    total_rows = 0
    years_sorted = sorted(set(int(y) for y in years))

    def _safe_str_int(x) -> str | None:
        if x is None:
            return None
        try:
            return str(int(x))
        except Exception:
            return str(x)

    def _row_id(pid: str, r: dict) -> str:
        rid = r.get("id")
        rid_s = _safe_str_int(rid)
        if rid_s:
            return f"{pid}:{rid_s}"
        # composite fallback
        t = _safe_str_int(r.get("idTipoRelator")) or "na"
        dd = r.get("dataDesignacao") or "na"
        cp = _safe_str_int(r.get("codigoParlamentar")) or "na"
        return f"{pid}:{t}:{dd}:{cp}"

    def _year_of_relatoria(r: dict, default_year: int) -> int:
        for key in ("dataDesignacao", "dataDestituicao", "dataApresentacaoProcesso"):
            v = r.get(key)
            if isinstance(v, str) and len(v) >= 4 and v[:4].isdigit():
                try:
                    return int(v[:4])
                except Exception:
                    pass
        return int(default_year)

    async with HttpClient(
        SENADO_BASE,
        rate_per_sec=settings.senado_rate,
        timeout=settings.http_timeout,
        user_agent=settings.user_agent,
    ) as hc:
        for y in years_sorted:
            idx_path = paths.index_file("senado", "processo", y)
            if not idx_path.exists():
                log.warning(f"[senado:relatorias] missing index for year={y}: {idx_path}")
                continue

            table = pq.read_table(idx_path, columns=["id"])
            pids: list[str] = sorted({str(r["id"]) for r in table.to_pylist()})
            if not pids:
                continue

            async def worker(pid: str) -> list[dict]:
                items = await senado_fetch_list(
                    hc,
                    "/processo/relatoria",
                    {"idProcesso": pid},
                    candidates=[["_list"], ["resultados"], ["Itens"]],  # liberal, like others
                )
                rows: list[dict] = []
                if not items:
                    return rows
                for rel in items:
                    payload_json = json.dumps(rel, ensure_ascii=False, separators=(",", ":"), sort_keys=True)
                    part_year = _year_of_relatoria(rel, y)
                    rows.append({
                        "source": "senado",
                        "entity": "relatorias",
                        "year": int(part_year),
                        "id": _row_id(pid, rel),
                        "url": f"{SENADO_BASE}/processo/relatoria?idProcesso={pid}",
                        "payload_json": payload_json,
                    })
                return rows

            lists, errs = await bounded_gather_pbar(
                pids, worker, concurrency=concurrency_processos, description=f"senado:relatorias:{y}"
            )
            if errs:
                log.warning(f"[senado:relatorias] year={y} errors={len(errs)} (partial write)")

            # flatten & group by partition year
            all_rows: list[dict] = [r for lst in lists for r in lst]
            by_year: dict[int, list[dict]] = defaultdict(list)
            for r in all_rows:
                by_year[int(r["year"])].append(r)

            for part_year, rows in sorted(by_year.items(), key=lambda kv: kv[0]):
                if not rows:
                    continue
                # guard pathological years (<=0) by rebucketing to the index year
                py = part_year if part_year > 0 else y
                if py != part_year:
                    for r in rows:
                        r["year"] = py
                write_relation_parts(
                    rows,
                    paths=paths,
                    manifest=manifest,
                    source="senado",
                    relation="relatorias",
                    year=int(py),
                    part_rows=50_000,
                    sort=True,
                )
                total_rows += len(rows)
                log.info(f"[senado:relatorias] wrote {len(rows)} rows into year={py}")

    log.info(f"[senado:relatorias] total rows={total_rows}")
    return total_rows
