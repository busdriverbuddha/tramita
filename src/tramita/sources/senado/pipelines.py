# tramita/sources/senado/pipelines.py

from datetime import date, timedelta
import json
import logging
from typing import Any, Iterable

from tramita.config import settings
from tramita.http.client import HttpClient
from tramita.log import setup_logging
from tramita.sources.base import bounded_gather_pbar
from tramita.sources.senado.client import senado_fetch, senado_fetch_list, _dig
from tramita.storage.manifest import SnapshotManifest
from tramita.storage.parquet import write_index_parquet, write_details_parts, write_relation_parts
from tramita.storage.paths import BronzePaths

# --- add near the top of the file ---
import unicodedata

log = logging.getLogger(__name__)

SENADO_BASE = settings.senado_base_url.rstrip("/")


def _slugify_natureza(s: str) -> str:
    """
    "Permanente" -> "permanente"
    "Temporária" -> "temporaria"
    "Conselho"   -> "conselho"
    "Mesa"       -> "mesa"
    "Plenário"   -> "plenario"
    "Órgão"      -> "orgao"
    """
    if not s:
        return ""
    s = unicodedata.normalize("NFKD", s)
    s = "".join(ch for ch in s if not unicodedata.combining(ch))
    return s.strip().lower()


def _year_from(*candidates: str | None, default: int) -> int:
    for v in candidates:
        if isinstance(v, str) and len(v) >= 4 and v[:4].isdigit():
            try:
                return int(v[:4])
            except Exception:
                pass
    return int(default)


def _first_present(d: dict, fields: tuple[str, ...] = (
    "id",
)) -> str | None:
    """
    Return the first present, non-null identifier field from `d`,
    normalized as a string. Tries int() cast first to strip
    leading zeros and enforce numeric form when possible.
    """
    for f in fields:
        if f in d and d[f] is not None:
            try:
                return str(int(d[f]))
            except Exception:
                return str(d[f])
    return None


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
    setup_logging()
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
    import json
    import logging
    from collections import defaultdict
    import pyarrow.parquet as pq

    from tramita.sources.senado.client import senado_fetch_list
    from tramita.http.client import HttpClient

    log = logging.getLogger(__name__)
    setup_logging()

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
        import hashlib
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

    codes_by_year = await parlamentares_codes_by_year_via_legislaturas(years)
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


async def parlamentares_codes_by_year_via_legislaturas(
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
            import logging
            logging.getLogger(__name__).warning(f"[senado:parlamentares] {len(errs)} erro(s) ao buscar legislaturas")

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
            ini = _d(leg["DataInicio"])
            fim = _d(leg["DataFim"])
        except Exception:
            continue
        bounds[n] = (ini, fim)
        if any(_year_hits_legislatura(y, ini, fim) for y in ys):
            selected.add(n)

    return sorted(selected), bounds


def _d(y: str) -> date:
    # Datas vêm como 'YYYY-MM-DD'
    return date.fromisoformat(y)


def _year_hits_legislatura(y: int, ini: date, fim: date) -> bool:
    ys, ye = date(y, 1, 1), date(y, 12, 31)
    return not (ye < ini or ys > fim)


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
    import pyarrow.parquet as pq
    import json
    setup_logging()
    log = logging.getLogger(__name__)

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


async def build_details_processos_iterative(
    paths: BronzePaths,
    manifest: SnapshotManifest,
    years: Iterable[int],
    *,
    concurrency: int = 16,
    max_rounds: int = 8,
) -> int:
    """
    Iteratively fetch /processo/{id} details starting from existing
    senado/processo/index/year=YYYY/ids.parquet. After each round,
    extract 'processosRelacionados[*].idOutroProcesso' from the freshly
    fetched payloads to form the next wave. Stop when no new ids.

    Each fetched detail is bucketed by its *natural* year:
      - prefer field 'ano'
      - fallback: documento.dataApresentacao[:4]
      - last resort: the smallest requested year
    Details are written to senado/processo/details/year=YYYY/part-*.parquet
    and recorded into the manifest.

    Returns total number of *unique* processos fetched.
    """
    import pyarrow.parquet as pq
    from collections import defaultdict

    setup_logging()
    log = logging.getLogger(__name__)

    years_sorted = sorted(set(int(y) for y in years))
    if not years_sorted:
        return 0

    # ---- Seed queue from existing per-year index files
    seed_ids: set[str] = set()
    for y in years_sorted:
        idx_path = paths.index_file("senado", "processo", y)
        if idx_path.exists():
            tbl = pq.read_table(idx_path, columns=["id"])
            seed_ids.update(str(r["id"]) for r in tbl.to_pylist())

    if not seed_ids:
        log.info("[senado:details_iter] no ids found in index; nothing to do")
        return 0

    async with HttpClient(
        SENADO_BASE,
        rate_per_sec=settings.senado_rate,
        timeout=settings.http_timeout,
        user_agent=settings.user_agent,
    ) as hc:
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

        def _related_ids(obj: dict) -> set[str]:
            rels = obj.get("processosRelacionados") or []
            out: set[str] = set()
            for it in rels:
                rid = it.get("idOutroProcesso")
                if rid is None:
                    continue
                try:
                    out.add(str(int(rid)))
                except Exception:
                    out.add(str(rid))
            return out

        seen: set[str] = set()          # fetched already (any round)
        frontier: set[str] = set(seed_ids)
        total_written = 0
        round_idx = 0

        while frontier and round_idx < max_rounds:
            round_idx += 1
            batch = sorted(pid for pid in frontier if pid not in seen)
            if not batch:
                break

            # --- Round fetch
            async def worker(pid: str):
                obj = await senado_fetch(hc, f"/processo/{pid}", {})
                year = _infer_year(obj)
                payload_json = json.dumps(obj, ensure_ascii=False, separators=(",", ":"), sort_keys=True)
                return year, {
                    "source": "senado",
                    "entity": "processo",
                    "year": year,
                    "id": pid,
                    "url": f"{SENADO_BASE}/processo/{pid}",
                    "payload_json": payload_json,
                }, _related_ids(obj)

            triplets, errs = await bounded_gather_pbar(
                batch, worker, concurrency=concurrency,
                description=f"senado:proc_details:round{round_idx}"
            )
            if errs:
                log.warning(f"[senado:details_iter] round={round_idx} errors={len(errs)} (continuing)")

            # --- Group by year and write parts deterministically
            by_year_rows: dict[int, list[dict]] = defaultdict(list)
            next_frontier: set[str] = set()

            for year, row, relset in triplets:
                by_year_rows[int(year)].append(row)
                next_frontier.update(relset)
                seen.add(row["id"])

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
                    f"[senado:details_iter] round={round_idx} year={year}"
                    f" wrote {len(rows)} rows in {len(parts)} part(s)"
                )

            # Prepare next wave: discovered minus already seen
            frontier = {pid for pid in next_frontier if pid not in seen}

            log.info(
                f"[senado:details_iter] round={round_idx} fetched={len(batch)} "
                f"discovered_next={len(frontier)} total_seen={len(seen)}"
            )

        log.info(f"[senado:details_iter] DONE after {round_idx} round(s), total unique detalhes={len(seen)}")

    return len(seen)


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
    import json
    from collections import defaultdict
    import logging
    import pyarrow.parquet as pq

    from tramita.sources.senado.client import senado_fetch_list
    from tramita.http.client import HttpClient
    from tramita.config import settings

    log = logging.getLogger(__name__)
    setup_logging()

    SENADO_BASE = settings.senado_base_url.rstrip("/")
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


# --- add below other build_* functions in the same file ---
async def build_colegiados(
    paths: BronzePaths,
    manifest: SnapshotManifest,
    years: Iterable[int],
) -> int:
    """
    Fetch the full list of committee types, then for each 'natureza' (permanente,
    temporaria, conselho, mesa, plenario, orgao) call:
        /comissao/lista/{slug}.json
    Extract each 'colegiado' as a Bronze detail row under entity="colegiado",
    partitioned by year = DataInicio[:4] (fallback to the lowest requested year).

    Writes: senado/colegiado/details/year=YYYY/part-*.parquet
    """
    from collections import defaultdict

    setup_logging()
    log = logging.getLogger(__name__)
    years_sorted = sorted(set(int(y) for y in years)) or [0]
    default_year = years_sorted[0]
    total_rows = 0

    async with HttpClient(
        SENADO_BASE,
        rate_per_sec=settings.senado_rate,
        timeout=settings.http_timeout,
        user_agent=settings.user_agent,
    ) as hc:
        # 1) get tipos (naturezas)
        tipos_obj = await senado_fetch(hc, "/dados/ListaTiposColegiado.json", {})
        tipo_list = (
            _dig(tipos_obj, ["ListaTiposColegiado", "TiposColegiado", "TipoColegiado"]) or []
        )

        # derive slugs from DescricaoNatureza (safe, future-proof)
        naturezas: list[str] = []
        for t in tipo_list:
            desc_nat = (t.get("DescricaoNatureza") or "").strip()
            slug = _slugify_natureza(desc_nat)
            if slug and slug not in naturezas:
                naturezas.append(slug)

        # sanity: only keep slugs the endpoint likely supports
        # (observed set)
        allowed = {"permanente", "temporaria", "conselho", "mesa", "plenario", "orgao"}
        naturezas = [n for n in naturezas if n in allowed]
        if not naturezas:
            log.warning("[senado:colegiados] no recognized 'natureza' slugs from ListaTiposColegiado.json")
            return 0

        # 2) for each natureza, fetch list and accumulate rows grouped by year
        by_year: dict[int, list[dict]] = defaultdict(list)

        def _iter_colegiados(obj: dict) -> list[dict]:
            """
            The shape tends to be:
            {"ListaBasicaComissoes":{"colegiado":{"colegiados":[{"colegiado":[{...},{...}]}]}}}
            We traverse liberally and collect all inner dicts under "*colegiado*".
            """
            out: list[dict] = []

            # try common paths first
            root = _dig(obj, ["ListaBasicaComissoes", "colegiado", "colegiados"])
            if isinstance(root, list):
                for bucket in root:
                    items = (bucket or {}).get("colegiado")
                    if isinstance(items, list):
                        out.extend([it for it in items if isinstance(it, dict)])

            # fallback: scan any dict/list for keys that look like "colegiado"
            if not out:
                def _scan(x):
                    if isinstance(x, dict):
                        for k, v in x.items():
                            if isinstance(v, list):
                                if k.lower().startswith("colegiad"):
                                    for it in v:
                                        if isinstance(it, dict):
                                            out.append(it)
                                else:
                                    for it in v:
                                        _scan(it)
                            elif isinstance(v, dict):
                                _scan(v)
                    elif isinstance(x, list):
                        for it in x:
                            _scan(it)
                _scan(obj)

            return out

        for nat in naturezas:
            path = f"/comissao/lista/{nat}.json"
            obj = await senado_fetch(hc, path, {})
            items = _iter_colegiados(obj)
            if not items:
                log.info(f"[senado:colegiados] {nat}: 0 items")
                continue

            for c in items:
                # id choices: CodigoColegiado (stable) or "id" string
                raw_id = c.get("CodigoColegiado") or c.get("id")
                cid = None
                if raw_id is not None:
                    try:
                        cid = str(int(raw_id))
                    except Exception:
                        cid = str(raw_id)
                if not cid:
                    # skip weird rows without ids
                    continue

                year = _year_from(c.get("DataInicio"), default=default_year)

                # full, deterministic payload
                payload_json = json.dumps(c, ensure_ascii=False, separators=(",", ":"), sort_keys=True)
                by_year[int(year)].append({
                    "source": "senado",
                    "entity": "colegiado",
                    "year": int(year),
                    "id": cid,
                    "url": f"{SENADO_BASE}/comissao/lista/{nat}.json",
                    "payload_json": payload_json,
                })

            log.info(f"[senado:colegiados] {nat}: collected {len(items)} items")

        # 3) write per-year parts
        wrote = 0
        for y, rows in sorted(by_year.items(), key=lambda kv: kv[0]):
            if not rows:
                continue
            parts = write_details_parts(
                rows,
                paths=paths,
                manifest=manifest,
                source="senado",
                entity="colegiado",
                year=int(y),
                part_rows=50_000,
                sort=True,
            )
            wrote += len(rows)
            log.info(f"[senado:colegiados] year={y} wrote {len(rows)} rows in {len(parts)} part(s)")

        total_rows = wrote

    log.info(f"[senado:colegiados] total rows={total_rows}")
    return total_rows


async def build_colegiados_votacoes(
    paths: BronzePaths,
    manifest: SnapshotManifest,
    years: Iterable[int],
    *,
    window_days: int = 30,
) -> int:
    """
    For each discovered colegiado (via senado/colegiado/details/*), fetch
    committee voting sessions in 30-day windows per requested year from:
        /votacaoComissao/comissao/{SIGLA}.json?dataInicio=YYYYMMDD&dataFim=YYYYMMDD

    Writes Bronze relation parts under:
        senado/votacoes_colegiado/year=YYYY/part-*.parquet
    Row id uses CodigoVotacao when present (stable), else a deterministic composite.

    Returns the total number of voting sessions written across all years.
    """
    import json
    import pyarrow.parquet as pq
    from collections import defaultdict
    from datetime import date, timedelta

    setup_logging()
    log = logging.getLogger(__name__)

    years_sorted = sorted(set(int(y) for y in years)) or []
    if not years_sorted:
        log.info("[senado:coleg_votos] no years requested; skipping")
        return 0

    # ---- 1) Discover committee SIGLAs from previously saved details
    siglas: set[str] = set()
    for y in years_sorted:
        details_dir = paths.details_part_dir("senado", "colegiado", y)
        if not details_dir.exists():
            continue
        parts = sorted(details_dir.glob("part-*.parquet"))
        for pf in parts:
            try:
                tbl = pq.read_table(pf, columns=["payload_json"])
            except Exception:
                continue
            for row in tbl.to_pylist():
                try:
                    obj = json.loads(row["payload_json"])
                except Exception:
                    continue
                s = (obj.get("SiglaColegiado") or obj.get("siglaColegiado") or "").strip()
                if s:
                    siglas.add(str(s))
    if not siglas:
        log.warning("[senado:coleg_votos] no committee siglas discovered; did you run build_colegiados first?")
        return 0

    # ---- 2) Fetch votes per SIGLA in windows per year
    def yyyymmdd(d: date) -> str:
        return f"{d.year:04d}{d.month:02d}{d.day:02d}"

    def _rows_from_response(sigla: str, obj: dict, default_year: int) -> list[dict]:
        # Typical path: VotacoesComissao -> Votacoes -> Votacao (list)
        root = _dig(obj, ["VotacoesComissao", "Votacoes", "Votacao"])
        items = root if isinstance(root, list) else []
        rows: list[dict] = []

        for v in items:
            # id: prefer CodigoVotacao
            raw_id = (v.get("CodigoVotacao") or v.get("codigoVotacao"))
            if raw_id is not None:
                try:
                    vid = str(int(raw_id))
                except Exception:
                    vid = str(raw_id)
            else:
                # deterministic composite fallback
                cr = v.get("CodigoReuniao") or v.get("codigoReuniao") or "na"
                dthr = v.get("DataHoraInicioReuniao") or v.get("dataHoraInicioReuniao") or "na"
                vid = f"{sigla}:{cr}:{dthr}"

            # year: prefer DataHoraInicioReuniao[:4]
            dthr = (v.get("DataHoraInicioReuniao") or v.get("dataHoraInicioReuniao") or "")
            part_year = default_year
            if isinstance(dthr, str) and len(dthr) >= 4 and dthr[:4].isdigit():
                try:
                    part_year = int(dthr[:4])
                except Exception:
                    part_year = default_year

            payload_json = json.dumps(v, ensure_ascii=False, separators=(",", ":"), sort_keys=True)
            rows.append({
                "source": "senado",
                "entity": "votacoes_colegiado",
                "year": int(part_year),
                "id": vid,
                "url": f"{SENADO_BASE}/votacaoComissao/comissao/{sigla}.json",
                "payload_json": payload_json,
            })
        return rows

    total_rows = 0

    async with HttpClient(
        SENADO_BASE,
        rate_per_sec=settings.senado_rate,
        timeout=settings.http_timeout,
        user_agent=settings.user_agent,
    ) as hc:
        for sigla in sorted(siglas):
            log.info(f"[senado:coleg_votos] SIGLA={sigla} years={years_sorted}")
            # Keep per-year de-dup set (CodigoVotacao or fallback id)
            dedup_by_year: dict[int, set[str]] = defaultdict(set)

            for y in years_sorted:
                year_start = date(y, 1, 1)
                year_end = date(y, 12, 31)
                cur = year_start

                by_year_rows: dict[int, list[dict]] = defaultdict(list)
                fetched_in_year = 0

                while cur <= year_end:
                    win_end = min(cur + timedelta(days=window_days - 1), year_end)
                    params = {
                        "dataInicio": yyyymmdd(cur),
                        "dataFim": yyyymmdd(win_end),
                    }
                    try:
                        obj = await senado_fetch(hc, f"/votacaoComissao/comissao/{sigla}.json", params)
                    except Exception as e:
                        log.warning(f"[senado:coleg_votos] {sigla} {cur}..{win_end} error: {e}")
                        cur = win_end + timedelta(days=1)
                        continue

                    rows = _rows_from_response(sigla, obj, default_year=y)
                    # Deduplicate within year
                    kept: list[dict] = []
                    for r in rows:
                        rid = r["id"]
                        part_y = int(r["year"])
                        if rid not in dedup_by_year[part_y]:
                            dedup_by_year[part_y].add(rid)
                            kept.append(r)

                    for r in kept:
                        by_year_rows[int(r["year"])].append(r)
                    fetched_in_year += len(kept)

                    cur = win_end + timedelta(days=1)

                # Write partitions for this sigla+year slice
                for part_year, rows in sorted(by_year_rows.items(), key=lambda kv: kv[0]):
                    if not rows:
                        continue
                    # Guard weird years (e.g., 0)
                    py = part_year if part_year > 0 else y
                    if py != part_year:
                        for r in rows:
                            r["year"] = py
                    write_relation_parts(
                        rows,
                        paths=paths,
                        manifest=manifest,
                        source="senado",
                        relation="votacoes_colegiado",
                        year=int(py),
                        part_rows=50_000,
                        sort=True,
                    )
                    total_rows += len(rows)
                    log.info(f"[senado:coleg_votos] {sigla} wrote {len(rows)} rows -> year={py}")

                if fetched_in_year:
                    log.info(f"[senado:coleg_votos] {sigla} year={y} kept={fetched_in_year}")

    log.info(f"[senado:coleg_votos] total rows written={total_rows}")
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
    import json
    from collections import defaultdict
    import logging
    import pyarrow.parquet as pq

    from tramita.sources.senado.client import senado_fetch_list
    from tramita.http.client import HttpClient
    from tramita.config import settings

    log = logging.getLogger(__name__)
    setup_logging()

    SENADO_BASE = settings.senado_base_url.rstrip("/")
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
