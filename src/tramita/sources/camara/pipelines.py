# tramita/sources/camara/pipelines.py

import hashlib
import json
import re

from datetime import date, timedelta
from typing import Any, Iterable, Sequence

import logging


from tramita.config import settings
from tramita.http.client import HttpClient, HttpError
from tramita.log import setup_logging
from tramita.sources.base import bounded_gather
from tramita.sources.camara.client import camara_fetch
from tramita.storage.manifest import SnapshotManifest
from tramita.storage.parquet import write_index_parquet, write_details_parts, write_relation_parts
from tramita.storage.paths import BronzePaths

log = logging.getLogger(__name__)


CAMARA_BASE = settings.camara_base_url.rstrip("/")
_DEP_RE = re.compile(r"/deputados/(\d+)")
_ORG_RE = re.compile(r"/orgaos/(\d+)")
_DATE_RE = re.compile(r"\d{4}-\d{2}-\d{2}")
_FR_RE = re.compile(r"/frentes/(\d+)")


def _extract_frente_ids(items: list[dict]) -> set[str]:
    ids: set[str] = set()
    for it in items or []:
        for k in ("idFrente", "id"):
            if it.get(k) is not None:
                try:
                    ids.add(str(int(it[k])))
                except Exception:
                    ids.add(str(it[k]))
        for k in ("uri", "uriFrente"):
            u = it.get(k)
            if isinstance(u, str):
                m = _FR_RE.search(u)
                if m:
                    ids.add(m.group(1))
    return ids


async def build_frentes_via_deputados(
    paths: BronzePaths,
    manifest: SnapshotManifest,
    years: Iterable[int],
    *,
    page_size: int = 100,
    concurrency_deputados: int = 16,
    concurrency_frentes: int = 16,
) -> tuple[int, int, int]:
    """
    1) Read camara/autores and camara/tramitacoes parts for the selected years,
       parse payload_json and collect relevant deputado IDs (+ first-seen year).
    2) For each deputado -> GET /deputados/{id}/frentes, write relation 'deputados/frentes'
       bucketed by first date seen in payload (fallback: earliest selected year).
       Collect frente IDs + first-seen year.
    3) Fetch /frentes/{fid} (details, year=0000) and /frentes/{fid}/membros
       (relation bucketed by first date in payload).
    Returns (#dep_frentes_rows, #frentes_details, #frentes_membros_rows).
    """
    import json
    import pyarrow.parquet as pq

    setup_logging()
    y0 = min(years) if years else 0
    default_bucket = y0

    first_seen_dep: dict[str, int] = {}

    # --- 1) read autores + tramitacoes parts to find deputados ---
    for y in years:
        for rel in ("autores", "tramitacoes"):
            d = paths.relation_part_dir("camara", rel, y)
            if not d.exists():
                continue
            for part in sorted(d.glob("part-*.parquet")):
                t = pq.read_table(part, columns=["payload_json"])
                for r in t.to_pylist():
                    try:
                        obj = json.loads(r["payload_json"])
                        dados = obj.get("dados") or []
                    except Exception:
                        continue
                    if rel == "autores":
                        deps, _ = _extract_author_targets(dados)
                    else:
                        deps = _extract_relatores_from_tramitacoes(dados)
                    for dep in deps:
                        first_seen_dep.setdefault(dep, y)

    dep_ids = sorted(first_seen_dep.keys(), key=int) if first_seen_dep else []
    if not dep_ids:
        log.info("[camara:frentes] no relevant deputados found; skipping")
        return (0, 0, 0)

    first_seen_frente: dict[str, int] = {}

    async with HttpClient(
        CAMARA_BASE, rate_per_sec=settings.camara_rate,
        timeout=settings.http_timeout, user_agent=settings.user_agent
    ) as hc:
        async def dep_worker(dep_id: str):
            dados = await camara_fetch(
                hc, f"/deputados/{dep_id}/frentes", {},
                itens=page_size, concurrency=8, fallback_follow_next=True
            )
            y = _bucket_year_for_items(dados, years, first_seen_dep.get(dep_id, default_bucket))
            row = {
                "source": "camara",
                "entity": "deputados/frentes",
                "year": y,
                "id": dep_id,
                "url": f"{CAMARA_BASE}/deputados/{dep_id}/frentes",
                "payload_json": json.dumps({"dados": dados}, ensure_ascii=False, separators=(",", ":"), sort_keys=True),
            }
            for fid in _extract_frente_ids(dados):
                first_seen_frente.setdefault(fid, y)
            return row

        dep_rows, dep_errs = await bounded_gather(dep_ids, dep_worker, concurrency=concurrency_deputados)
        if dep_errs:
            log.warning(f"[camara:deputados/frentes] errors={len(dep_errs)}")

    # write deputados/frentes grouped by year
    dep_count = 0
    for y in sorted({r["year"] for r in dep_rows}):
        rows_y = [r for r in dep_rows if r["year"] == y]
        parts = write_relation_parts(
            rows_y, paths=paths, manifest=manifest,
            source="camara", relation="deputados/frentes", year=int(y),
            part_rows=50_000, sort=True
        )
        dep_count += len(rows_y)
        log.info(f"[camara:deputados/frentes] year={y} wrote {len(rows_y)} rows in {len(parts)} part(s)")

    # --- 3) fetch frentes details + membros only for discovered IDs ---
    frentes_by_year: dict[int, list[str]] = {}
    for fid, y in first_seen_frente.items():
        frentes_by_year.setdefault(y, []).append(fid)

    fr_det_count = fr_mem_count = 0

    async with HttpClient(
        CAMARA_BASE, rate_per_sec=settings.camara_rate,
        timeout=settings.http_timeout, user_agent=settings.user_agent
    ) as hc:
        # details (year=0000)
        async def fr_det_worker(fid: str):
            url = f"/frentes/{fid}"
            # txt = await hc.get_text(url)
            # try:
            #     obj = json.loads(txt)
            #     dados = obj.get("dados") or []
            # except Exception as e:
            #     raise RuntimeError(f"{pid} relacionadas JSON decode error: {e}") from e
            dados = await camara_fetch(
                hc, url, {},
                itens=100, concurrency=8, fallback_follow_next=True
            )
            return {
                "source": "camara",
                "entity": "frentes",
                "year": 0,
                "id": fid,
                "url": CAMARA_BASE + url,
                "payload_json": json.dumps(
                    {"dados": dados}, ensure_ascii=False, separators=(",", ":"), sort_keys=True
                ),
            }

        det_ids = sorted(first_seen_frente.keys(), key=int)
        det_rows, det_errs = await bounded_gather(det_ids, fr_det_worker, concurrency=concurrency_frentes)
        if det_errs:
            log.warning(f"[camara:frentes(details)] errors={len(det_errs)}")
        if det_rows:
            dp = write_details_parts(
                det_rows, paths=paths, manifest=manifest,
                source="camara", entity="frentes", year=0,
                part_rows=50_000, sort=True
            )
            fr_det_count = len(det_rows)
            log.info(f"[camara:frentes] wrote {len(det_rows)} details in {len(dp)} part(s) → year=0000")

        # membros (bucket by first date in list; fallback=first-seen year)
        async def fr_mem_worker(fid: str, yy: int):
            dados = await camara_fetch(
                hc, f"/frentes/{fid}/membros", {},
                itens=page_size, concurrency=8, fallback_follow_next=True
            )
            y = _bucket_year_for_items(dados, years, yy)
            return {
                "source": "camara",
                "entity": "frentes/membros",
                "year": y,
                "id": fid,
                "url": f"{CAMARA_BASE}/frentes/{fid}/membros",
                "payload_json": json.dumps({"dados": dados}, ensure_ascii=False, separators=(",", ":"), sort_keys=True),
            }

        for y in sorted(frentes_by_year):
            fids = sorted(set(frentes_by_year[y]), key=int)

            async def w(fid: str, yy: int = y):
                return await fr_mem_worker(fid, yy)
            mem_rows, mem_errs = await bounded_gather(fids, w, concurrency=concurrency_frentes)
            if mem_errs:
                log.warning(f"[camara:frentes/membros] year={y} errors={len(mem_errs)}")
            if mem_rows:
                mp = write_relation_parts(
                    mem_rows, paths=paths, manifest=manifest,
                    source="camara", relation="frentes/membros", year=y,
                    part_rows=50_000, sort=True
                )
                fr_mem_count += len(mem_rows)
                log.info(f"[camara:frentes/membros] year={y} wrote {len(mem_rows)} rows in {len(mp)} part(s)")

    return dep_count, fr_det_count, fr_mem_count


def _hash_take(pid: str, keep_num: int | None, keep_den: int | None) -> bool:
    if not keep_num or not keep_den:
        return True
    h = hashlib.sha256(pid.encode("utf-8")).hexdigest()
    val = int(h[:8], 16)  # 32-bit slice is enough
    return (val % keep_den) < keep_num


def _parse_fraction(spec: str | None) -> tuple[int | None, int | None]:
    # spec like "1/200" => (1, 200)
    if not spec:
        return None, None
    a, b = spec.split("/", 1)
    return int(a), int(b)


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


async def _list_ids_generic(
    hc: HttpClient,
    path: str,
    *,
    page_size: int = 100,
    id_fields: tuple[str, ...] = ("id",),
    extra_params: dict[str, Any] | None = None,
    supports_ordering: bool = True,
) -> list[str]:
    params: dict[str, Any] = {}
    if supports_ordering:
        params |= {"ordem": "ASC", "ordenarPor": "id"}
    if extra_params:
        params |= extra_params
    try:
        dados = await camara_fetch(
            hc, path, params, itens=page_size, concurrency=8, fallback_follow_next=True
        )
    except HttpError as e:
        if supports_ordering and (e.status_code in (400, 422)):
            # retry without unsupported order params
            dados = await camara_fetch(
                hc, path, extra_params or {}, itens=page_size, concurrency=8, fallback_follow_next=True
            )
        else:
            raise
    out: list[str] = []
    for d in dados or []:
        oid = next((d.get(f) for f in id_fields if d.get(f) is not None), None)
        if oid is None:
            continue
        try:
            out.append(str(int(oid)))
        except Exception:
            out.append(str(oid))
    try:
        return sorted(set(out), key=int)
    except Exception:
        return sorted(set(out), key=str)


def _year_range_params(year: int) -> dict[str, Any]:
    return {
        "dataApresentacaoInicio": f"{year}-01-01",
        "dataApresentacaoFim": f"{year}-12-31",
        "ordem": "ASC",
        "ordenarPor": "id",
    }


async def build_index_proposicoes(paths: BronzePaths, year: int, *, page_size: int = 100) -> int:
    """
    List proposições for a year and write ids.parquet under .../index/year=YYYY/
    Returns the number of IDs written.
    """
    setup_logging()
    idx_path = paths.index_file("camara", "proposicoes", year)

    async with HttpClient(
        CAMARA_BASE,
        rate_per_sec=settings.camara_rate,
        timeout=settings.http_timeout,
        user_agent=settings.user_agent,
    ) as hc:
        params = _year_range_params(year)
        # Use the 'last link' strategy the way you described
        dados = await camara_fetch(
            hc, "/proposicoes",
            params | {"ordem": "ASC", "ordenarPor": "id"},
            itens=page_size,
            concurrency=8,
            fallback_follow_next=True,
        )

    rows = []
    for d in dados:
        pid = str(d["id"])
        url = d.get("uri") or f"{CAMARA_BASE}/proposicoes/{pid}"
        rows.append({
            "source": "camara",
            "entity": "proposicoes",
            "year": year,
            "id": pid,
            "url": url,
            "payload_json": json.dumps(
                {"dados": dados}, ensure_ascii=False, separators=(",", ":"), sort_keys=True
            ),
        })

    n = write_index_parquet(rows, idx_path)
    log.info(f"[camara:index] year={year} proposicoes={n} -> {idx_path}")
    return n


async def _fetch_detail(hc: HttpClient, year: int, rec: dict) -> dict:
    pid = str(rec["id"])
    # Prefer the provided URL; fallback to canonical
    url = rec.get("url") or f"{CAMARA_BASE}/proposicoes/{pid}"
    dados = await camara_fetch(
        hc, url, {},
        itens=100, concurrency=8, fallback_follow_next=True
    )
    # Keep raw JSON text; we also pass 'year' so the writer can sort
    return {
        "source": "camara",
        "entity": "proposicoes",
        "year": year,
        "id": pid,
        "url": url,
        "payload_json": json.dumps(
            {"dados": dados}, ensure_ascii=False, separators=(",", ":"), sort_keys=True
        ),
    }


async def build_details_proposicoes(
    paths: BronzePaths,
    manifest: SnapshotManifest,
    year: int,
    *,
    concurrency: int = 20
) -> int:
    """
    Read ids.parquet for the given year and write details parts under .../details/year=YYYY/
    Returns total rows written.
    """
    import pyarrow.parquet as pq
    setup_logging()

    idx_path = paths.index_file("camara", "proposicoes", year)
    if not idx_path.exists():  # <-- add this guard
        log.warning(f"[camara:details] missing index for year={year}: {idx_path}")
        return 0

    table = pq.read_table(idx_path)  # schema has: source, entity, id, url
    ids = [{"id": r["id"], "url": r["url"]} for r in table.to_pylist()]

    async with HttpClient(
        CAMARA_BASE,
        rate_per_sec=settings.camara_rate,
        timeout=settings.http_timeout,
        user_agent=settings.user_agent,
    ) as hc:
        async def worker(rec):
            try:
                return await _fetch_detail(hc, year, rec)
            except HttpError as e:
                raise RuntimeError(f"{rec['id']} {e.status_code} {e}") from e

        rows, errs = await bounded_gather(ids, worker, concurrency=concurrency)

    if errs:
        log.warning(f"[camara:details] year={year} errors={len(errs)} (will still write successful rows)")

    parts = write_details_parts(
        rows,
        paths=paths,
        manifest=manifest,
        source="camara",
        entity="proposicoes",
        year=year,
        part_rows=50_000,
        sort=True,
    )
    log.info(f"[camara:details] year={year} wrote {len(rows)} rows in {len(parts)} part(s)")
    return len(rows)


def _iter_date_windows(start: date, end: date, *, days: int) -> list[tuple[date, date]]:
    """Left-closed, right-closed windows: [d0, d1]."""
    out: list[tuple[date, date]] = []
    d = start
    while d <= end:
        d1 = min(d + timedelta(days=days - 1), end)
        out.append((d, d1))
        d = d1 + timedelta(days=1)
    return out


async def build_index_proposicoes_tramitadas(
    paths: BronzePaths,
    years: Iterable[int],
    *,
    window_days: int = 30,
    page_size: int = 100,
    concurrency_windows: int = 4,
    include_sigla: Sequence[str] | None = None,
    sample: str | None = None,  # e.g. "1/200"
    start_date: date | None = None,
    end_date: date | None = None,
) -> int:
    """
    Build the index of proposições that had *tramitação* between the first and last
    year in `years`, scanning 30-day windows. Dedup by id. Bucket by the year of the
    window where the id first appears (deterministic).
    """
    setup_logging()

    y0, y1 = min(years), max(years)
    start = start_date or date(y0, 1, 1)
    end = end_date or date(y1, 12, 31)
    windows = _iter_date_windows(start, end, days=window_days)
    keep_num, keep_den = _parse_fraction(sample)

    async with HttpClient(
        CAMARA_BASE,
        rate_per_sec=settings.camara_rate,
        timeout=settings.http_timeout,
        user_agent=settings.user_agent,
    ) as hc:
        async def worker(win: tuple[date, date]):
            d0, d1 = win
            base_params = {
                "dataInicio": d0.isoformat(),
                "dataFim": d1.isoformat(),
                "ordem": "ASC",
                "ordenarPor": "id",
            }
            all_rows: list[dict] = []
            if include_sigla:
                # Fetch each type separately (reduces payload upstream)
                for st in include_sigla:
                    params = base_params | {"siglaTipo": st}
                    dados = await camara_fetch(
                        hc, "/proposicoes", params,
                        itens=page_size, concurrency=8, fallback_follow_next=True,
                    )
                    all_rows.extend(dados)
            else:
                dados = await camara_fetch(
                    hc, "/proposicoes", base_params,
                    itens=page_size, concurrency=8, fallback_follow_next=True,
                )
                all_rows.extend(dados)
            return d0, d1, all_rows

        results, errs = await bounded_gather(windows, worker, concurrency=concurrency_windows)

    if errs:
        log.warning(
            f"[camara:index-tram] windows_errors={len(errs)} (continuing with successes)")

    # Deterministic order across windows
    results.sort(key=lambda r: (r[0], r[1]))

    # First-seen wins
    seen: set[str] = set()
    by_year: dict[int, list[dict]] = {}

    for d0, d1, dados in results:
        bucket_year = d0.year
        for d in dados:
            pid = str(d["id"])
            if include_sigla:
                if (d.get("siglaTipo") or "") not in set(include_sigla):
                    continue
            # optional: sampling
            if not _hash_take(pid, keep_num, keep_den):
                continue
            if pid in seen:
                continue
            seen.add(pid)
            url = d.get("uri") or f"{CAMARA_BASE}/proposicoes/{pid}"
            row = {
                "source": "camara",
                "entity": "proposicoes",
                # note: bucket year (first-seen tramitação window)
                "year": bucket_year,
                "id": pid,
                "url": url,
            }
            by_year.setdefault(bucket_year, []).append(row)

    total = 0
    for y in sorted(by_year):
        idx_path = paths.index_file("camara", "proposicoes", y)
        n = write_index_parquet(by_year[y], idx_path)
        log.info(f"[camara:index-tram] year={y} proposicoes={n} -> {idx_path}")
        total += n

    log.info(
        f"[camara:index-tram] total_unique_ids={len(seen)} across years {y0}-{y1}")
    return total


def _extract_author_targets(items: list[dict]) -> tuple[set[str], set[str]]:
    """
    From autores items, return (deputados_ids, orgaos_ids) as strings.
    Tries URIs first; falls back to id fields when available.
    """
    deps: set[str] = set()
    orgs: set[str] = set()

    for a in items or []:
        # scan common URI-bearing keys
        for k in ("uri", "uriAutor", "urlAutor", "uriOrgao"):
            u = a.get(k)
            if isinstance(u, str):
                m = _DEP_RE.search(u)
                if m:
                    deps.add(m.group(1))
                m = _ORG_RE.search(u)
                if m:
                    orgs.add(m.group(1))
        # fallbacks if URIs are missing
        if "idAutor" in a and a["idAutor"] is not None:
            try:
                deps.add(str(int(a["idAutor"])))
            except Exception:
                pass
        if "codOrgaoAutor" in a and a["codOrgaoAutor"] is not None:
            # Câmara órgão codes are numeric in this API
            try:
                orgs.add(str(int(a["codOrgaoAutor"])))
            except Exception:
                pass
    return deps, orgs


async def _build_simple_relation(
    paths: BronzePaths,
    manifest: SnapshotManifest,
    years: Iterable[int],
    *,
    relation: str,                 # "temas" | "tramitacoes"
    endpoint_fmt: str,             # e.g. "/proposicoes/{pid}/temas"
    concurrency_props: int = 16,
) -> int:
    """
    Generic helper: for each year, read proposicoes index and fetch a single
    non-paginated relation endpoint; store one row per proposicao under
    camara/<relation>/year=YYYY/.
    Returns total relation rows written.
    """
    import pyarrow.parquet as pq
    setup_logging()
    total_rel = 0

    async with HttpClient(
        CAMARA_BASE,
        rate_per_sec=settings.camara_rate,
        timeout=settings.http_timeout,
        user_agent=settings.user_agent,
    ) as hc:
        for y in years:
            idx_path = paths.index_file("camara", "proposicoes", y)
            if not idx_path.exists():
                log.warning(f"[camara:{relation}] missing index for year={y}: {idx_path}")
                continue

            table = pq.read_table(idx_path)
            ids = [str(r["id"]) for r in table.to_pylist()]

            async def rel_worker(pid: str) -> dict[str, Any]:
                path = endpoint_fmt.format(pid=pid)
                # txt = await hc.get_text(path)
                # try:
                #     obj = json.loads(txt)
                #     dados = obj.get("dados") if isinstance(obj, dict) else obj
                #     if dados is None:
                #         # fall back to raw obj if schema differs
                #         dados = obj
                # except Exception as e:
                #     raise RuntimeError(f"{pid} {relation} JSON decode error: {e}") from e
                dados = await camara_fetch(
                    hc, path, {},
                    itens=100, concurrency=8, fallback_follow_next=True
                )
                payload = json.dumps({"dados": dados}, ensure_ascii=False, separators=(",", ":"), sort_keys=True)
                return {
                    "source": "camara",
                    "entity": relation,   # relation name for manifest
                    "year": y,
                    "id": pid,            # key the relation by proposicao id
                    "url": CAMARA_BASE + path,
                    "payload_json": payload,
                }

            rel_rows, rel_errs = await bounded_gather(ids, rel_worker, concurrency=concurrency_props)
            if rel_errs:
                log.warning(f"[camara:{relation}] year={y} relation_errors={len(rel_errs)}")

            parts = write_relation_parts(
                rel_rows,
                paths=paths,
                manifest=manifest,
                source="camara",
                relation=relation,
                year=y,
                part_rows=50_000,
                sort=True,
            )
            total_rel += len(rel_rows)
            log.info(f"[camara:{relation}] year={y} wrote {len(rel_rows)} rows in {len(parts)} part(s)")

    log.info(f"[camara:{relation}] total_rows={total_rel}")
    return total_rel


async def build_temas_relations(
    paths: BronzePaths,
    manifest: SnapshotManifest,
    years: Iterable[int],
    *,
    concurrency_props: int = 16,
) -> int:
    return await _build_simple_relation(
        paths, manifest, years,
        relation="temas",
        endpoint_fmt="/proposicoes/{pid}/temas",
        concurrency_props=concurrency_props,
    )


async def build_tramitacoes_relations(
    paths: BronzePaths,
    manifest: SnapshotManifest,
    years: Iterable[int],
    *,
    concurrency_props: int = 16,
) -> int:
    return await _build_simple_relation(
        paths, manifest, years,
        relation="tramitacoes",
        endpoint_fmt="/proposicoes/{pid}/tramitacoes",
        concurrency_props=concurrency_props,
    )


async def build_autores_relations_and_entities(
    paths: BronzePaths,
    manifest: SnapshotManifest,
    years: Iterable[int],
    *,
    page_size: int = 100,
    concurrency_props: int = 16,
    concurrency_deputados: int = 16,
    concurrency_orgaos: int = 8,
    fetch_orgaos: bool = True,
    fetch_deputados: bool = True,
) -> tuple[int, int, int]:
    """
    For each year, read proposicoes index, fetch autores relation, store one row per proposicao
    under camara/autores/year=YYYY/, and fetch unique /deputados/{id} and /orgaos/{id} details.

    Returns (n_rel_rows, n_deputados, n_orgaos).
    """
    setup_logging()
    total_rel = 0
    total_deps = 0
    total_orgs = 0

    # Track first-seen year for each author so we bucket details deterministically
    first_seen_dep: dict[str, int] = {}
    first_seen_org: dict[str, int] = {}

    import pyarrow.parquet as pq

    async with HttpClient(
        CAMARA_BASE,
        rate_per_sec=settings.camara_rate,
        timeout=settings.http_timeout,
        user_agent=settings.user_agent,
    ) as hc:

        # -------- 1) fetch autores per proposicao (by year) --------
        for y in years:
            idx_path = paths.index_file("camara", "proposicoes", y)
            if not idx_path.exists():
                log.warning(f"[camara:autores] missing index for year={y}: {idx_path}")
                continue

            table = pq.read_table(idx_path)
            ids = [str(r["id"]) for r in table.to_pylist()]

            async def rel_worker(pid: str):
                path = f"/proposicoes/{pid}/autores"
                # autores endpoint is NOT paginated; fetch once and read "dados"
                dados = await camara_fetch(
                    hc, path, {},
                    itens=100, concurrency=8, fallback_follow_next=True
                )

                # record first-seen author ids → bucket year
                deps, orgs = _extract_author_targets(dados)
                for d in deps:
                    first_seen_dep.setdefault(d, y)
                for o in orgs:
                    first_seen_org.setdefault(o, y)

                # store one relation row per proposicao (payload = {"dados":[...]} )
                payload = json.dumps({"dados": dados}, ensure_ascii=False, separators=(",", ":"), sort_keys=True)
                return {
                    "source": "camara",
                    "entity": "autores",   # relation name for manifest
                    "year": y,
                    "id": pid,             # key the relation by proposicao id
                    "url": CAMARA_BASE + path,
                    "payload_json": payload,
                }

            rel_rows, rel_errs = await bounded_gather(ids, rel_worker, concurrency=concurrency_props)
            if rel_errs:
                log.warning(f"[camara:autores] year={y} relation_errors={len(rel_errs)}")

            # write relation parts (grouped under camara/autores/year=YYYY/)
            parts = write_relation_parts(
                rel_rows,
                paths=paths,
                manifest=manifest,
                source="camara",
                relation="autores",
                year=y,
                part_rows=50_000,
                sort=True,
            )
            total_rel += len(rel_rows)
            log.info(f"[camara:autores] year={y} wrote {len(rel_rows)} rows in {len(parts)} part(s)")

        # -------- 2) fetch unique author entities (deputados, orgaos) --------
        # We’ll bucket each entity into the first year it appeared above.
        # Build {year: [ids...]} for deterministic output.
        dep_by_year: dict[int, list[str]] = {}
        org_by_year: dict[int, list[str]] = {}
        for dep, y in first_seen_dep.items():
            dep_by_year.setdefault(y, []).append(dep)
        for org, y in first_seen_org.items():
            org_by_year.setdefault(y, []).append(org)

        async def dep_worker(yy: int, dep_id: str):
            url = f"/deputados/{dep_id}"
            dados = await camara_fetch(
                hc, url, {},
                itens=100, concurrency=8, fallback_follow_next=True
            )
            return {
                "source": "camara",
                "entity": "deputados",
                "year": yy,
                "id": dep_id,
                "url": CAMARA_BASE + url,
                "payload_json": json.dumps(
                    {"dados": dados}, ensure_ascii=False, separators=(",", ":"), sort_keys=True
                ),
            }

        async def org_worker(yy: int, org_id: str):
            url = f"/orgaos/{org_id}"
            dados = await camara_fetch(
                hc, url, {},
                itens=100, concurrency=8, fallback_follow_next=True
            )
            return {
                "source": "camara",
                "entity": "orgaos",
                "year": yy,
                "id": org_id,
                "url": CAMARA_BASE + url,
                "payload_json": json.dumps(
                    {"dados": dados}, ensure_ascii=False, separators=(",", ":"), sort_keys=True
                ),
            }

        # Deputados
        if fetch_deputados:
            for y in sorted(dep_by_year):
                dep_ids: list[str] = sorted(dep_by_year[y], key=int)

                async def dep_id_worker(dep_id: str, yy: int = y) -> dict[str, Any]:
                    return await dep_worker(yy, dep_id)

                dep_rows, dep_errs = await bounded_gather(
                    dep_ids,
                    dep_id_worker,
                    concurrency=concurrency_deputados,
                )
                if dep_errs:
                    log.warning(f"[camara:deputados] year={y} errors={len(dep_errs)}")
                parts = write_details_parts(
                    dep_rows,
                    paths=paths,
                    manifest=manifest,
                    source="camara",
                    entity="deputados",
                    year=y,
                    part_rows=50_000,
                    sort=True,
                )
                total_deps += len(dep_rows)
                log.info(f"[camara:deputados] year={y} wrote {len(dep_rows)} rows in {len(parts)} part(s)")

        # Órgãos
        if fetch_orgaos:
            for y in sorted(org_by_year):
                org_ids: list[str] = sorted(org_by_year[y], key=int)

                async def org_id_worker(org_id: str, yy: int = y) -> dict[str, Any]:
                    return await org_worker(yy, org_id)

                org_rows, org_errs = await bounded_gather(
                    org_ids,
                    org_id_worker,
                    concurrency=concurrency_orgaos,
                )
                if org_errs:
                    log.warning(f"[camara:orgaos] year={y} errors={len(org_errs)}")
                parts = write_details_parts(
                    org_rows,
                    paths=paths,
                    manifest=manifest,
                    source="camara",
                    entity="orgaos",
                    year=y,
                    part_rows=50_000,
                    sort=True,
                )
                total_orgs += len(org_rows)
                log.info(f"[camara:orgaos] year={y} wrote {len(org_rows)} rows in {len(parts)} part(s)")

    log.info(f"[camara:autores] relations={total_rel} deputados={total_deps} orgaos={total_orgs}")
    return total_rel, total_deps, total_orgs


async def expand_index_via_relacionadas(
    paths: BronzePaths,
    manifest: SnapshotManifest,
    years: Iterable[int],
    *,
    concurrency: int = 16,
    max_rounds: int = 6,
) -> int:
    """
    Iteratively follow /proposicoes/{id}/relacionadas from the current index until
    no new proposicoes are found. For each origin id we write one relation row under
    camara/relacionadas/year=YYYY/. Any newly discovered proposicao ids are bucketed
    deterministically into the origin's year (first-seen wins), merged back into the
    per-year index parquet, and may trigger further rounds.

    Returns total number of *new* proposicoes added across all rounds.
    """
    import pyarrow.parquet as pq

    setup_logging()
    # ---- 1) load current index into id -> year map (and per-year URL map, if needed) ----
    id_year: dict[str, int] = {}
    for y in years:
        idx_path = paths.index_file("camara", "proposicoes", y)
        if not idx_path.exists():
            continue
        t = pq.read_table(idx_path, columns=["id", "url", "source", "entity"])
        for r in t.to_pylist():
            pid = str(r["id"])
            id_year.setdefault(pid, y)  # keep first bucket for determinism

    if not id_year:
        log.info("[camara:relacionadas] no seed ids in index; skipping expansion")
        return 0

    # Track which ids we've already fetched /relacionadas for in THIS run
    fetched: set[str] = set()
    total_new = 0

    async with HttpClient(
        CAMARA_BASE,
        rate_per_sec=settings.camara_rate,
        timeout=settings.http_timeout,
        user_agent=settings.user_agent,
    ) as hc:

        async def rel_worker(pid: str, yy: int):
            path = f"/proposicoes/{pid}/relacionadas"
            dados = await camara_fetch(
                hc, path, {},
                itens=100, concurrency=8, fallback_follow_next=True
            )
            # Collect new proposicao ids from 'dados'
            new_ids: list[str] = []
            for it in dados or []:
                try:
                    rid = str(int(it.get("id")))
                except Exception:
                    rid = str(it.get("id"))
                if rid and (rid not in id_year):
                    new_ids.append(rid)

            # One relation row per origin
            payload = json.dumps({"dados": dados}, ensure_ascii=False, separators=(",", ":"), sort_keys=True)
            row = {
                "source": "camara",
                "entity": "relacionadas",
                "year": yy,
                "id": pid,
                "url": CAMARA_BASE + path,
                "payload_json": payload,
            }
            return row, new_ids

        # ---- 2) iterate rounds until fixed point or max_rounds ----
        for round_idx in range(1, max_rounds + 1):
            # frontier = all known ids that haven't had /relacionadas fetched yet
            frontier_by_year: dict[int, list[str]] = {}
            for pid, yy in id_year.items():
                if pid not in fetched:
                    frontier_by_year.setdefault(yy, []).append(pid)

            if not frontier_by_year:
                log.info("[camara:relacionadas] fixed point reached; no pending frontier")
                break

            frontier_size = sum(len(v) for v in frontier_by_year.values())
            log.info(f"[camara:relacionadas] round={round_idx} frontier={frontier_size}")

            newly_found_by_year: dict[int, list[str]] = {}

            # process frontier grouped by the bucket year of the origin
            for y in sorted(frontier_by_year):
                ids = frontier_by_year[y]

                async def rel_id_worker(pid: str, yy: int = y):
                    return await rel_worker(pid, yy)

                results, errs = await bounded_gather(ids, rel_id_worker, concurrency=concurrency)
                if errs:
                    log.warning(f"[camara:relacionadas] year={y} relation_errors={len(errs)}")

                # split (row, new_ids) → write rows + accumulate new ids
                rel_rows = []
                new_ids_accum: list[str] = []
                for row, new_ids in results:
                    rel_rows.append(row)
                    new_ids_accum.extend(new_ids)

                # write relation rows for this origin-year
                parts = write_relation_parts(
                    rel_rows,
                    paths=paths,
                    manifest=manifest,   # manifest from outer scope; will exist where this is called
                    source="camara",
                    relation="relacionadas",
                    year=y,
                    part_rows=50_000,
                    sort=True,
                )
                log.info(f"[camara:relacionadas] year={y} wrote {len(rel_rows)} rows in {len(parts)} part(s)")

                # mark fetched
                fetched.update(ids)

                # bucket new ids into *origin* year (first-seen wins)
                if new_ids_accum:
                    for rid in new_ids_accum:
                        if rid not in id_year:
                            id_year[rid] = y
                            newly_found_by_year.setdefault(y, []).append(rid)

            if not newly_found_by_year:
                log.info(f"[camara:relacionadas] round={round_idx} found no new ids; stopping")
                break

            # ---- 3) merge new ids into per-year index parquet ----
            for y, new_list in newly_found_by_year.items():
                idx_path = paths.index_file("camara", "proposicoes", y)
                existing: list[dict] = []
                if idx_path.exists():
                    t = pq.read_table(idx_path)
                    existing = [{**r, "year": y} for r in t.to_pylist()]

                have = {str(r["id"]) for r in existing}
                additions = []
                for pid in new_list:
                    if pid not in have:
                        additions.append({
                            "source": "camara",
                            "entity": "proposicoes",
                            "year": y,
                            "id": pid,
                            "url": f"{CAMARA_BASE}/proposicoes/{pid}",
                        })

                if additions:
                    merged = existing + additions
                    # write deterministically (function sorts)
                    n = write_index_parquet(merged, idx_path)
                    log.info(f"[camara:index-rel] year={y} merged index → {n} ids ({len(additions)} new)")

            round_new = sum(len(v) for v in newly_found_by_year.values())
            total_new += round_new

    log.info(f"[camara:relacionadas] total_new_ids={total_new}")
    return total_new


def _extract_orgaos_from_tramitacoes(items: list[dict]) -> set[str]:
    """
    From tramitacoes 'dados', return órgão IDs found in 'uriOrgao'.
    """
    out: set[str] = set()
    for it in items or []:
        u = it.get("uriOrgao")
        if isinstance(u, str):
            m = _ORG_RE.search(u)
            if m:
                out.add(m.group(1))
    return out


async def build_tramitacoes_relations_and_orgaos(
    paths: BronzePaths,
    manifest: SnapshotManifest,
    years: Iterable[int],
    *,
    concurrency_props: int = 16,
    concurrency_orgaos: int = 8,
    concurrency_deputados: int = 16,
) -> tuple[int, int, int]:
    """
    Fetch /proposicoes/{id}/tramitacoes (relation rows) and, for every órgão
    referenced via 'uriOrgao', fetch /orgaos/{id} once; additionally, when a
    'uriUltimoRelator' is present, fetch the relator profile via /deputados/{id}.
    All entity fetches are bucketed by the origin proposição's first-seen year.

    Returns (n_relation_rows, n_orgaos_rows, n_deputados_rows).
    """
    import pyarrow.parquet as pq

    setup_logging()
    total_rel = 0
    total_orgs = 0
    total_deps = 0

    # Track first-seen bucket year for determinism
    first_seen_org: dict[str, int] = {}
    first_seen_dep: dict[str, int] = {}

    async with HttpClient(
        CAMARA_BASE,
        rate_per_sec=settings.camara_rate,
        timeout=settings.http_timeout,
        user_agent=settings.user_agent,
    ) as hc:
        # -------- 1) fetch tramitacoes per proposicao (by year) --------
        for y in years:
            idx_path = paths.index_file("camara", "proposicoes", y)
            if not idx_path.exists():
                log.warning(f"[camara:tramitacoes] missing index for year={y}: {idx_path}")
                continue

            table = pq.read_table(idx_path)
            ids = [str(r["id"]) for r in table.to_pylist()]

            async def rel_worker(pid: str) -> dict[str, Any]:
                path = f"/proposicoes/{pid}/tramitacoes"
                dados = await camara_fetch(
                    hc, path, {},
                    itens=100, concurrency=8, fallback_follow_next=True
                )
                # collect órgãos and relatores referenced here and remember first-seen bucket year
                for org_id in _extract_orgaos_from_tramitacoes(dados):
                    first_seen_org.setdefault(org_id, y)
                for dep_id in _extract_relatores_from_tramitacoes(dados):
                    first_seen_dep.setdefault(dep_id, y)

                payload = json.dumps({"dados": dados}, ensure_ascii=False, separators=(",", ":"), sort_keys=True)
                return {
                    "source": "camara",
                    "entity": "tramitacoes",
                    "year": y,
                    "id": pid,
                    "url": CAMARA_BASE + path,
                    "payload_json": payload,
                }

            rel_rows, rel_errs = await bounded_gather(ids, rel_worker, concurrency=concurrency_props)
            if rel_errs:
                log.warning(f"[camara:tramitacoes] year={y} relation_errors={len(rel_errs)}")

            parts = write_relation_parts(
                rel_rows,
                paths=paths,
                manifest=manifest,
                source="camara",
                relation="tramitacoes",
                year=y,
                part_rows=50_000,
                sort=True,
            )
            total_rel += len(rel_rows)
            log.info(f"[camara:tramitacoes] year={y} wrote {len(rel_rows)} rows in {len(parts)} part(s)")

        # -------- 2) fetch unique órgão entities (grouped by first-seen year) --------
        org_by_year: dict[int, list[str]] = {}
        for org, y in first_seen_org.items():
            org_by_year.setdefault(y, []).append(org)

        for y in sorted(org_by_year):
            org_ids: list[str] = sorted(org_by_year[y], key=int)

            async def org_worker(org_id: str, yy: int = y) -> dict[str, Any]:
                url = f"/orgaos/{org_id}"
                dados = await camara_fetch(
                    hc, url, {},
                    itens=100, concurrency=8, fallback_follow_next=True
                )
                return {
                    "source": "camara",
                    "entity": "orgaos",
                    "year": yy,
                    "id": org_id,
                    "url": CAMARA_BASE + url,
                    "payload_json": json.dumps(
                        {"dados": dados}, ensure_ascii=False, separators=(",", ":"), sort_keys=True
                    ),
                }

            org_rows, org_errs = await bounded_gather(org_ids, org_worker, concurrency=concurrency_orgaos)
            if org_errs:
                log.warning(f"[camara:orgaos<-tramitacoes] year={y} errors={len(org_errs)}")

            parts = write_details_parts(
                org_rows,
                paths=paths,
                manifest=manifest,
                source="camara",
                entity="orgaos",
                year=y,
                part_rows=50_000,
                sort=True,
            )
            total_orgs += len(org_rows)
            log.info(f"[camara:orgaos<-tramitacoes] year={y} wrote {len(org_rows)} rows in {len(parts)} part(s)")

        # -------- 3) fetch unique deputado entities (grouped by first-seen year) ------
        dep_by_year: dict[int, list[str]] = {}
        for dep, y in first_seen_dep.items():
            dep_by_year.setdefault(y, []).append(dep)

        for y in sorted(dep_by_year):
            dep_ids: list[str] = sorted(dep_by_year[y], key=int)

            async def dep_worker(dep_id: str, yy: int = y) -> dict[str, Any]:
                url = f"/deputados/{dep_id}"
                dados = await camara_fetch(
                    hc, url, {},
                    itens=100, concurrency=8, fallback_follow_next=True
                )
                return {
                    "source": "camara",
                    "entity": "deputados",
                    "year": yy,
                    "id": dep_id,
                    "url": CAMARA_BASE + url,
                    "payload_json": json.dumps(
                        {"dados": dados}, ensure_ascii=False, separators=(",", ":"), sort_keys=True
                    ),
                }

            dep_rows, dep_errs = await bounded_gather(dep_ids, dep_worker, concurrency=concurrency_deputados)
            if dep_errs:
                log.warning(f"[camara:deputados<-tramitacoes] year={y} errors={len(dep_errs)}")

            parts = write_details_parts(
                dep_rows,
                paths=paths,
                manifest=manifest,
                source="camara",
                entity="deputados",
                year=y,
                part_rows=50_000,
                sort=True,
            )
            total_deps += len(dep_rows)
            log.info(f"[camara:deputados<-tramitacoes] year={y} wrote {len(dep_rows)} rows in {len(parts)} part(s)")

    log.info(f"[camara:tramitacoes+orgaos+relatores] relations={total_rel} orgaos={total_orgs} deputados={total_deps}")
    return total_rel, total_orgs, total_deps


async def build_all_orgaos(
    paths: BronzePaths,
    manifest: SnapshotManifest,
    *,
    page_size: int = 100,
    list_concurrency: int = 8,
    fetch_concurrency: int = 16,
    year_bucket: int = 0,
) -> int:
    """
    Fetch the full órgão catalog:
      1) GET /orgaos with pagination to enumerate ids.
      2) GET /orgaos/{id} for each id (concurrently).
    Store under camara/orgaos/details/year=0000/.
    Returns number of órgãos written.
    """
    setup_logging()

    async with HttpClient(
        CAMARA_BASE,
        rate_per_sec=settings.camara_rate,
        timeout=settings.http_timeout,
        user_agent=settings.user_agent,
    ) as hc:
        # 1) List all órgãos (paginated)
        dados = await camara_fetch(
            hc,
            "/orgaos",
            {"ordem": "ASC", "ordenarPor": "id"},
            itens=page_size,
            concurrency=list_concurrency,
            fallback_follow_next=True,
        )

        # Accept either 'id' or 'idOrgao' defensively
        ids: list[str] = []
        for d in dados:
            oid = d.get("id")
            if oid is None:
                oid = d.get("idOrgao")
            if oid is None:
                continue
            try:
                ids.append(str(int(oid)))
            except Exception:
                ids.append(str(oid))

        ids = sorted(set(ids), key=int)  # determinism

        # 2) Fetch details for each órgão id
        async def worker(org_id: str) -> dict[str, Any]:
            url = f"/orgaos/{org_id}"
            # txt = await hc.get_text(url)
            # try:
            #     obj = json.loads(txt)
            #     dados = obj.get("dados") or []
            # except Exception as e:
            #     raise RuntimeError(f"{pid} relacionadas JSON decode error: {e}") from e
            dados = await camara_fetch(
                hc, url, {},
                itens=100, concurrency=8, fallback_follow_next=True
            )
            return {
                "source": "camara",
                "entity": "orgaos",
                "year": year_bucket,
                "id": org_id,
                "url": CAMARA_BASE + url,
                "payload_json": json.dumps(
                    {"dados": dados}, ensure_ascii=False, separators=(",", ":"), sort_keys=True
                ),
            }

        rows, errs = await bounded_gather(ids, worker, concurrency=fetch_concurrency)
        if errs:
            log.warning(f"[camara:orgaos(all)] detail_errors={len(errs)} (continuing with successes)")

    parts = write_details_parts(
        rows,
        paths=paths,
        manifest=manifest,
        source="camara",
        entity="orgaos",
        year=year_bucket,
        part_rows=50_000,
        sort=True,
    )

    log.info(f"[camara:orgaos(all)] wrote {len(rows)} rows in {len(parts)} part(s) → year={year_bucket:04d}")
    return len(rows)


async def build_votacoes_votos_orientacoes(
    paths: BronzePaths,
    manifest: SnapshotManifest,
    years: Iterable[int],
    *,
    page_size: int = 100,
    concurrency_props: int = 12,      # concurrent proposições -> /votacoes
    concurrency_children: int = 16,   # concurrent votações -> /votos + /orientacoes
) -> tuple[int, int, int]:
    """
    For each year bucket of proposições:
      - GET /proposicoes/{pid}/votacoes (paginated) and store one relation row per proposição
        under camara/votacoes/year=YYYY/ (payload = {"dados":[...]}).
      - Collect votação IDs discovered and, bucketed by the same proposição year,
        fetch all pages of:
          * GET /votacoes/{vid}/votos        -> store under camara/votos/year=YYYY/
          * GET /votacoes/{vid}/orientacoes  -> store under camara/orientacoes/year=YYYY/

    Returns (n_proposicao_votacoes_rows, n_votos_rows, n_orientacoes_rows).
    """
    import pyarrow.parquet as pq

    setup_logging()
    total_rel_rows = 0
    total_votos_rows = 0
    total_orients_rows = 0

    async with HttpClient(
        CAMARA_BASE,
        rate_per_sec=settings.camara_rate,
        timeout=settings.http_timeout,
        user_agent=settings.user_agent,
    ) as hc:
        # -------- 1) /proposicoes/{id}/votacoes per year (paginated) --------
        votacoes_by_year: dict[int, list[str]] = {}  # {year: [votacao_id,...]}
        for y in years:
            idx_path = paths.index_file("camara", "proposicoes", y)
            if not idx_path.exists():
                log.warning(f"[camara:votacoes] missing index for year={y}: {idx_path}")
                continue

            table = pq.read_table(idx_path)
            prop_ids: list[str] = [str(r["id"]) for r in table.to_pylist()]

            async def prop_worker(pid: str) -> dict[str, Any]:
                # Use pagination helper; order by id for determinism.
                dados = await camara_fetch(
                    hc,
                    f"/proposicoes/{pid}/votacoes",
                    {"ordem": "ASC", "ordenarPor": "id"},
                    itens=page_size,
                    concurrency=8,
                    fallback_follow_next=True,
                )
                # Collect votação IDs (string per docs)
                for it in dados or []:
                    vid = it.get("id")
                    if vid is None:
                        continue
                    votacoes_by_year.setdefault(y, []).append(str(vid))

                payload = json.dumps({"dados": dados}, ensure_ascii=False, separators=(",", ":"), sort_keys=True)
                return {
                    "source": "camara",
                    "entity": "votacoes",   # relation name in manifest/paths
                    "year": y,
                    "id": pid,              # key row by proposição id
                    "url": f"{CAMARA_BASE}/proposicoes/{pid}/votacoes",
                    "payload_json": payload,
                }

            rel_rows, rel_errs = await bounded_gather(prop_ids, prop_worker, concurrency=concurrency_props)
            if rel_errs:
                log.warning(f"[camara:votacoes] year={y} relation_errors={len(rel_errs)}")

            parts = write_relation_parts(
                rel_rows,
                paths=paths,
                manifest=manifest,
                source="camara",
                relation="votacoes",
                year=y,
                part_rows=50_000,
                sort=True,
            )
            total_rel_rows += len(rel_rows)
            log.info(f"[camara:votacoes] year={y} wrote {len(rel_rows)} rows in {len(parts)} part(s)")

        # Normalize/unique votação IDs per year (deterministic order)
        for y in list(votacoes_by_year.keys()):
            vids = sorted(set(votacoes_by_year[y]))
            votacoes_by_year[y] = vids

        # -------- 2) For each votação id -> fetch votos + orientacoes (paginated) --------
        for y in sorted(votacoes_by_year.keys()):
            vid_list = votacoes_by_year[y]

            async def child_worker(vid: str):
                # Fetch both paginated lists serially per vid (bounded by concurrency_children across vids)
                votos = await camara_fetch(
                    hc,
                    f"/votacoes/{vid}/votos",
                    {},  # no special ordering documented beyond pagination; links drive order
                    itens=page_size,
                    concurrency=8,
                    fallback_follow_next=True,
                )
                orients = await camara_fetch(
                    hc,
                    f"/votacoes/{vid}/orientacoes",
                    {},
                    itens=page_size,
                    concurrency=8,
                    fallback_follow_next=True,
                )
                votos_row = {
                    "source": "camara",
                    "entity": "votos",
                    "year": y,
                    "id": str(vid),
                    "url": f"{CAMARA_BASE}/votacoes/{vid}/votos",
                    "payload_json": json.dumps(
                        {"dados": votos}, ensure_ascii=False, separators=(",", ":"), sort_keys=True
                    ),
                }
                orients_row = {
                    "source": "camara",
                    "entity": "orientacoes",
                    "year": y,
                    "id": str(vid),
                    "url": f"{CAMARA_BASE}/votacoes/{vid}/orientacoes",
                    "payload_json": json.dumps(
                        {"dados": orients}, ensure_ascii=False, separators=(",", ":"), sort_keys=True
                    ),
                }
                return votos_row, orients_row

            results, child_errs = await bounded_gather(vid_list, child_worker, concurrency=concurrency_children)
            if child_errs:
                log.warning(f"[camara:votos+orientacoes] year={y} errors={len(child_errs)}")

            votos_rows = [r[0] for r in results]
            orient_rows = [r[1] for r in results]

            if votos_rows:
                vp = write_relation_parts(
                    votos_rows,
                    paths=paths,
                    manifest=manifest,
                    source="camara",
                    relation="votos",
                    year=y,
                    part_rows=50_000,
                    sort=True,
                )
                total_votos_rows += len(votos_rows)
                log.info(f"[camara:votos] year={y} wrote {len(votos_rows)} rows in {len(vp)} part(s)")

            if orient_rows:
                op = write_relation_parts(
                    orient_rows,
                    paths=paths,
                    manifest=manifest,
                    source="camara",
                    relation="orientacoes",
                    year=y,
                    part_rows=50_000,
                    sort=True,
                )
                total_orients_rows += len(orient_rows)
                log.info(f"[camara:orientacoes] year={y} wrote {len(orient_rows)} rows in {len(op)} part(s)")

    log.info(
        f"[camara:votacoes+votos+orientacoes] votacoes_rows={total_rel_rows} "
        f"votos_rows={total_votos_rows} orientacoes_rows={total_orients_rows}"
    )
    return total_rel_rows, total_votos_rows, total_orients_rows


async def build_index_eventos(
    paths: BronzePaths,
    years: Iterable[int],
    *,
    window_days: int = 30,
    page_size: int = 100,
    concurrency_windows: int = 4,
    start_date: date | None = None,
    end_date: date | None = None,
) -> int:
    """
    Scan /eventos using [dataInicio, dataFim] windows (like proposições),
    dedup by id, and bucket into the year of the window start (deterministic).
    Writes ids.parquet under camara/eventos/index/year=YYYY/.
    """
    setup_logging()

    y0, y1 = min(years), max(years)
    start = start_date or date(y0, 1, 1)
    end = end_date or date(y1, 12, 31)
    windows = _iter_date_windows(start, end, days=window_days)

    async with HttpClient(
        CAMARA_BASE,
        rate_per_sec=settings.camara_rate,
        timeout=settings.http_timeout,
        user_agent=settings.user_agent,
    ) as hc:
        async def worker(win: tuple[date, date]):
            d0, d1 = win
            params = {
                "dataInicio": d0.isoformat(),
                "dataFim": d1.isoformat(),
                "ordem": "ASC",
                "ordenarPor": "id",
            }
            dados = await camara_fetch(
                hc, "/eventos", params,
                itens=page_size, concurrency=8, fallback_follow_next=True,
            )
            return d0, d1, dados

        results, errs = await bounded_gather(windows, worker, concurrency=concurrency_windows)

    if errs:
        log.warning(f"[camara:eventos-index] windows_errors={len(errs)} (continuing)")

    # Deterministic order across windows
    results.sort(key=lambda r: (r[0], r[1]))

    seen: set[str] = set()
    by_year: dict[int, list[dict]] = {}

    for d0, d1, dados in results:
        bucket_year = d0.year
        for d in dados or []:
            try:
                eid = str(int(d.get("id")))
            except Exception:
                eid = str(d.get("id"))
            if not eid or eid in seen:
                continue
            seen.add(eid)
            url = d.get("uri") or f"{CAMARA_BASE}/eventos/{eid}"
            by_year.setdefault(bucket_year, []).append({
                "source": "camara",
                "entity": "eventos",
                "year": bucket_year,
                "id": eid,
                "url": url,
            })

    total = 0
    for y in sorted(by_year):
        idx_path = paths.index_file("camara", "eventos", y)
        n = write_index_parquet(by_year[y], idx_path)
        log.info(f"[camara:eventos-index] year={y} eventos={n} -> {idx_path}")
        total += n

    log.info(f"[camara:eventos-index] total_unique_ids={len(seen)} across years {y0}-{y1}")
    return total


async def build_details_eventos(
    paths: BronzePaths,
    manifest: SnapshotManifest,
    year: int,
    *,
    concurrency: int = 20,
) -> int:
    """
    Read camara/eventos/index/year=YYYY/ids.parquet and fetch /eventos/{id} details.
    Store under camara/eventos/details/year=YYYY/.
    """
    import pyarrow.parquet as pq
    setup_logging()

    idx_path = paths.index_file("camara", "eventos", year)
    if not idx_path.exists():
        log.warning(f"[camara:eventos-details] missing index for year={year}: {idx_path}")
        return 0

    table = pq.read_table(idx_path)
    ids = [str(r["id"]) for r in table.to_pylist()]

    async with HttpClient(
        CAMARA_BASE,
        rate_per_sec=settings.camara_rate,
        timeout=settings.http_timeout,
        user_agent=settings.user_agent,
    ) as hc:
        async def worker(eid: str):
            url = f"/eventos/{eid}"
            # txt = await hc.get_text(url)
            # try:
            #     obj = json.loads(txt)
            #     dados = obj.get("dados") or []
            # except Exception as e:
            #     raise RuntimeError(f"{pid} relacionadas JSON decode error: {e}") from e
            dados = await camara_fetch(
                hc, url, {},
                itens=100, concurrency=8, fallback_follow_next=True
            )
            return {
                "source": "camara",
                "entity": "eventos",
                "year": year,
                "id": eid,
                "url": CAMARA_BASE + url,
                "payload_json": json.dumps(
                    {"dados": dados}, ensure_ascii=False, separators=(",", ":"), sort_keys=True
                ),
            }

        rows, errs = await bounded_gather(ids, worker, concurrency=concurrency)

    if errs:
        log.warning(f"[camara:eventos-details] year={year} errors={len(errs)}")

    parts = write_details_parts(
        rows,
        paths=paths,
        manifest=manifest,
        source="camara",
        entity="eventos",
        year=year,
        part_rows=50_000,
        sort=True,
    )
    log.info(f"[camara:eventos-details] year={year} wrote {len(rows)} rows in {len(parts)} part(s)")
    return len(rows)


async def build_eventos_relations(
    paths: BronzePaths,
    manifest: SnapshotManifest,
    years: Iterable[int],
    *,
    page_size: int = 100,
    concurrency_events: int = 16,
) -> tuple[int, int, int, int]:
    """
    For each evento id (per-year index), fetch the paginated relations:
      - /eventos/{id}/pauta         -> relation 'eventos/pauta'
      - /eventos/{id}/votacoes      -> relation 'eventos/votacoes'
      - /eventos/{id}/deputados     -> relation 'eventos/deputados'
      - /eventos/{id}/orgaos        -> relation 'eventos/orgaos'
    We write one row per evento for each relation (payload = {"dados":[...]}).
    Returns (#pauta_rows, #votacoes_rows, #deputados_rows, #orgaos_rows).
    """
    import pyarrow.parquet as pq
    setup_logging()

    total_pauta = total_vot = total_deps = total_orgs = 0

    async with HttpClient(
        CAMARA_BASE,
        rate_per_sec=settings.camara_rate,
        timeout=settings.http_timeout,
        user_agent=settings.user_agent,
    ) as hc:
        for y in years:
            idx_path = paths.index_file("camara", "eventos", y)
            if not idx_path.exists():
                log.warning(f"[camara:eventos-rel] missing index for year={y}: {idx_path}")
                continue

            table = pq.read_table(idx_path)
            eids: list[str] = [str(r["id"]) for r in table.to_pylist()]

            async def rel_worker(eid: str):
                async def fetch_list(path: str) -> list[dict]:
                    return await camara_fetch(
                        hc, path, {}, itens=page_size, concurrency=8, fallback_follow_next=True
                    )

                pauta = await fetch_list(f"/eventos/{eid}/pauta")
                ev_vot = await fetch_list(f"/eventos/{eid}/votacoes")
                deps = await fetch_list(f"/eventos/{eid}/deputados")
                orgs = await fetch_list(f"/eventos/{eid}/orgaos")

                def row(rel: str, data: list[dict]) -> dict[str, Any]:
                    return {
                        "source": "camara",
                        "entity": rel,   # e.g., "eventos/pauta"
                        "year": y,
                        "id": eid,       # key by evento id
                        "url": f"{CAMARA_BASE}/eventos/{eid}/{rel.split('/', 1)[1]}",
                        "payload_json": json.dumps(
                            {"dados": data}, ensure_ascii=False, separators=(",", ":"), sort_keys=True
                        ),
                    }

                return (
                    row("eventos/pauta", pauta),
                    row("eventos/votacoes", ev_vot),
                    row("eventos/deputados", deps),
                    row("eventos/orgaos", orgs),
                )

            results, errs = await bounded_gather(eids, rel_worker, concurrency=concurrency_events)
            if errs:
                log.warning(f"[camara:eventos-rel] year={y} errors={len(errs)}")

            pauta_rows = [r[0] for r in results]
            votacoes_rows = [r[1] for r in results]
            deputados_rows = [r[2] for r in results]
            orgaos_rows = [r[3] for r in results]

            if pauta_rows:
                pp = write_relation_parts(
                    pauta_rows, paths=paths, manifest=manifest,
                    source="camara", relation="eventos/pauta", year=y,
                    part_rows=50_000, sort=True,
                )
                total_pauta += len(pauta_rows)
                log.info(f"[camara:eventos/pauta] year={y} wrote {len(pauta_rows)} rows in {len(pp)} part(s)")

            if votacoes_rows:
                vp = write_relation_parts(
                    votacoes_rows, paths=paths, manifest=manifest,
                    source="camara", relation="eventos/votacoes", year=y,
                    part_rows=50_000, sort=True,
                )
                total_vot += len(votacoes_rows)
                log.info(f"[camara:eventos/votacoes] year={y} wrote {len(votacoes_rows)} rows in {len(vp)} part(s)")

            if deputados_rows:
                dp = write_relation_parts(
                    deputados_rows, paths=paths, manifest=manifest,
                    source="camara", relation="eventos/deputados", year=y,
                    part_rows=50_000, sort=True,
                )
                total_deps += len(deputados_rows)
                log.info(f"[camara:eventos/deputados] year={y} wrote {len(deputados_rows)} rows in {len(dp)} part(s)")

            if orgaos_rows:
                op = write_relation_parts(
                    orgaos_rows, paths=paths, manifest=manifest,
                    source="camara", relation="eventos/orgaos", year=y,
                    part_rows=50_000, sort=True,
                )
                total_orgs += len(orgaos_rows)
                log.info(f"[camara:eventos/orgaos] year={y} wrote {len(orgaos_rows)} rows in {len(op)} part(s)")

    log.info(
        f"[camara:eventos-rel] pauta={total_pauta} votacoes={total_vot} deputados={total_deps} orgaos={total_orgs}"
    )
    return total_pauta, total_vot, total_deps, total_orgs


async def _list_all_orgaos_ids(hc: HttpClient, *, page_size: int = 100) -> list[str]:
    """
    Enumerate every órgão id using /orgaos (paginated). Returns numeric-string ids, sorted.
    """
    dados = await camara_fetch(
        hc,
        "/orgaos",
        {"ordem": "ASC", "ordenarPor": "id"},
        itens=page_size,
        concurrency=8,
        fallback_follow_next=True,
    )
    ids: list[str] = []
    for d in dados or []:
        oid = d.get("id")
        if oid is None:
            oid = d.get("idOrgao")
        if oid is None:
            continue
        try:
            ids.append(str(int(oid)))
        except Exception:
            ids.append(str(oid))
    return sorted(set(ids), key=int)


async def build_orgaos_membros(
    paths: BronzePaths,
    manifest: SnapshotManifest,
    years: Iterable[int],
    *,
    page_size: int = 100,
    concurrency_orgaos: int = 16,
    year_bucket: int | None = None,
) -> int:
    """
    Fetch /orgaos/{id}/membros for all órgãos (paginated) and store one row per órgão
    under camara/orgaos/membros/year=YYYY/. Defaults to bucketing in the first year provided.
    """
    setup_logging()
    y0 = min(years) if years else 0
    bucket = y0 if year_bucket is None else year_bucket
    total = 0

    async with HttpClient(
        CAMARA_BASE,
        rate_per_sec=settings.camara_rate,
        timeout=settings.http_timeout,
        user_agent=settings.user_agent,
    ) as hc:
        org_ids = await _list_all_orgaos_ids(hc, page_size=page_size)

        async def worker(oid: str) -> dict[str, Any]:
            dados = await camara_fetch(
                hc,
                f"/orgaos/{oid}/membros",
                {},  # relies on pagination links; no date filters documented here
                itens=page_size,
                concurrency=8,
                fallback_follow_next=True,
            )
            return {
                "source": "camara",
                "entity": "orgaos/membros",
                "year": bucket,
                "id": oid,
                "url": f"{CAMARA_BASE}/orgaos/{oid}/membros",
                "payload_json": json.dumps({"dados": dados}, ensure_ascii=False, separators=(",", ":"), sort_keys=True),
            }

        rows, errs = await bounded_gather(org_ids, worker, concurrency=concurrency_orgaos)
        if errs:
            log.warning(f"[camara:orgaos/membros] errors={len(errs)} (continuing with successes)")

    if rows:
        parts = write_relation_parts(
            rows,
            paths=paths,
            manifest=manifest,
            source="camara",
            relation="orgaos/membros",
            year=bucket,
            part_rows=50_000,
            sort=True,
        )
        total = len(rows)
        log.info(f"[camara:orgaos/membros] year={bucket} wrote {total} rows in {len(parts)} part(s)")

    return total


async def expand_index_eventos_via_orgaos(
    paths: BronzePaths,
    years: Iterable[int],
    *,
    window_days: int = 30,
    page_size: int = 100,
    concurrency_windows: int = 4,
    concurrency_orgaos: int = 12,
    start_date: date | None = None,
    end_date: date | None = None,
) -> int:
    """
    Use /orgaos/{id}/eventos to discover evento IDs within date windows and merge
    them into camara/eventos/index/year=YYYY/ (bucket = window start year).
    Returns number of *new* evento ids added across all years.
    """
    setup_logging()
    y0, y1 = min(years), max(years)
    start = start_date or date(y0, 1, 1)
    end = end_date or date(y1, 12, 31)
    windows = _iter_date_windows(start, end, days=window_days)

    import pyarrow.parquet as pq

    # load existing index → {year: set(ids)}
    have: dict[int, set[str]] = {}
    for y in years:
        idx_path = paths.index_file("camara", "eventos", y)
        ids_y: set[str] = set()
        if idx_path.exists():
            t = pq.read_table(idx_path, columns=["id"])
            ids_y = {str(r["id"]) for r in t.to_pylist()}
        have[y] = ids_y

    total_new = 0

    async with HttpClient(
        CAMARA_BASE,
        rate_per_sec=settings.camara_rate,
        timeout=settings.http_timeout,
        user_agent=settings.user_agent,
    ) as hc:
        org_ids = await _list_all_orgaos_ids(hc, page_size=page_size)

        async def win_worker(win: tuple[date, date]):
            d0, d1 = win
            params = {
                "dataInicio": d0.isoformat(),
                "dataFim": d1.isoformat(),
                "ordem": "ASC",
                "ordenarPor": "id",
            }

            async def org_worker(oid: str) -> list[str]:
                itens = await camara_fetch(
                    hc, f"/orgaos/{oid}/eventos", params,
                    itens=page_size, concurrency=8, fallback_follow_next=True,
                )
                out: list[str] = []
                for it in itens or []:
                    vid = it.get("id")
                    if vid is None:
                        continue
                    try:
                        out.append(str(int(vid)))
                    except Exception:
                        out.append(str(vid))
                return out

            results, errs = await bounded_gather(org_ids, org_worker, concurrency=concurrency_orgaos)
            if errs:
                log.warning(f"[camara:orgaos→eventos] win={d0}..{d1} errors={len(errs)}")

            bucket_year = d0.year
            discovered = set(x for lst in results for x in lst)
            return bucket_year, discovered

        win_results, win_errs = await bounded_gather(windows, win_worker, concurrency=concurrency_windows)
        if win_errs:
            log.warning(f"[camara:orgaos→eventos] window_errors={len(win_errs)} (continuing)")

    # merge and write
    for y, discovered in sorted(win_results, key=lambda x: x[0]):
        if not discovered:
            continue
        idx_path = paths.index_file("camara", "eventos", y)
        existing = have.get(y, set())
        additions = sorted(discovered - existing, key=int if all(s.isdigit() for s in discovered) else str)
        if not additions:
            continue

        # rebuild full list for the year and write deterministically
        merged_rows = (
            [{"source": "camara", "entity": "eventos", "year": y, "id": pid, "url": f"{CAMARA_BASE}/eventos/{pid}"}]
            for pid
            in sorted(existing | discovered, key=int if all(s.isdigit() for s in existing | discovered) else str)
        )
        # materialize generator
        merged_rows = list(merged_rows)
        n = write_index_parquet(merged_rows, idx_path)
        have[y] = existing | discovered
        total_new += len(additions)
        log.info(f"[camara:eventos-index<-orgaos] year={y} +{len(additions)} ids → {n} total")

    log.info(f"[camara:orgaos→eventos] total_new_eventos={total_new}")
    return total_new


async def build_orgaos_votacoes_relations(
    paths: BronzePaths,
    manifest: SnapshotManifest,
    years: Iterable[int],
    *,
    page_size: int = 100,
    concurrency_orgaos: int = 12,
    year_bucket: int | None = None,
) -> int:
    """
    Fetch /orgaos/{id}/votacoes (paginated) for all órgãos and store one row per órgão
    under camara/orgaos/votacoes/year=YYYY/. Useful as an auxiliary discovery path for votação ids.
    """
    setup_logging()
    y0 = min(years) if years else 0
    bucket = y0 if year_bucket is None else year_bucket
    total = 0

    async with HttpClient(
        CAMARA_BASE,
        rate_per_sec=settings.camara_rate,
        timeout=settings.http_timeout,
        user_agent=settings.user_agent,
    ) as hc:
        org_ids = await _list_all_orgaos_ids(hc, page_size=page_size)

        async def worker(oid: str) -> dict[str, Any]:
            dados = await camara_fetch(
                hc,
                f"/orgaos/{oid}/votacoes",
                {"ordem": "ASC", "ordenarPor": "id"},
                itens=page_size,
                concurrency=8,
                fallback_follow_next=True,
            )
            return {
                "source": "camara",
                "entity": "orgaos/votacoes",
                "year": bucket,
                "id": oid,
                "url": f"{CAMARA_BASE}/orgaos/{oid}/votacoes",
                "payload_json": json.dumps({"dados": dados}, ensure_ascii=False, separators=(",", ":"), sort_keys=True),
            }

        rows, errs = await bounded_gather(org_ids, worker, concurrency=concurrency_orgaos)
        if errs:
            log.warning(f"[camara:orgaos/votacoes] errors={len(errs)} (continuing)")

    if rows:
        parts = write_relation_parts(
            rows,
            paths=paths,
            manifest=manifest,
            source="camara",
            relation="orgaos/votacoes",
            year=bucket,
            part_rows=50_000,
            sort=True,
        )
        total = len(rows)
        log.info(f"[camara:orgaos/votacoes] year={bucket} wrote {total} rows in {len(parts)} part(s)")

    return total


def _extract_relatores_from_tramitacoes(items: list[dict]) -> set[str]:
    """
    From tramitacoes 'dados', return deputado IDs found in 'uriUltimoRelator'
    (fallback to 'uriRelator' if present).
    """
    out: set[str] = set()
    for it in items or []:
        for k in ("uriUltimoRelator", "uriRelator"):
            u = it.get(k)
            if isinstance(u, str):
                m = _DEP_RE.search(u)
                if m:
                    out.add(m.group(1))
    return out


async def build_deputados_catalog(
    paths: BronzePaths,
    manifest: SnapshotManifest,
    *,
    page_size: int = 100,
    list_concurrency: int = 8,
    fetch_concurrency: int = 16,
    year_bucket: int = 0,
) -> int:
    """
    Catálogo + detalhes de /deputados, estático em year=0000.
    """
    setup_logging()

    async with HttpClient(
        CAMARA_BASE,
        rate_per_sec=settings.camara_rate,
        timeout=settings.http_timeout,
        user_agent=settings.user_agent,
    ) as hc:
        ids = await _list_ids_generic(hc, "/deputados", page_size=page_size)

        async def worker(dep_id: str) -> dict[str, Any]:
            url = f"/deputados/{dep_id}"
            dados = await camara_fetch(
                hc, url, {},
                itens=100, concurrency=8, fallback_follow_next=True
            )
            return {
                "source": "camara",
                "entity": "deputados",
                "year": year_bucket,
                "id": dep_id,
                "url": CAMARA_BASE + url,
                "payload_json": json.dumps(
                    {"dados": dados}, ensure_ascii=False, separators=(",", ":"), sort_keys=True
                ),
            }

        rows, errs = await bounded_gather(ids, worker, concurrency=fetch_concurrency)
        if errs:
            log.warning(f"[camara:deputados(all)] detail_errors={len(errs)} (continuing)")

    parts = write_details_parts(
        rows,
        paths=paths,
        manifest=manifest,
        source="camara",
        entity="deputados",
        year=year_bucket,
        part_rows=50_000,
        sort=True,
    )
    log.info(f"[camara:deputados(all)] wrote {len(rows)} rows in {len(parts)} part(s) → year={year_bucket:04d}")
    return len(rows)


async def build_deputados_relations(
    paths: BronzePaths,
    manifest: SnapshotManifest,
    years: Iterable[int],
    *,
    page_size: int = 100,
    concurrency_deputados: int = 16,
) -> tuple[int, int, int]:
    """
    Para cada deputado:
      - /deputados/{id}/orgaos      -> relation 'deputados/orgaos'
      - /deputados/{id}/historico   -> relation 'deputados/historico'
      - /deputados/{id}/frentes     -> relation 'deputados/frentes'
    Cada relação é bucketizada no 'primeiro avistamento' inferido das datas do payload.
    """
    setup_logging()
    y0 = min(years) if years else 0
    default_bucket = y0
    tot_orgs = tot_hist = tot_frentes = 0

    async with HttpClient(
        CAMARA_BASE,
        rate_per_sec=settings.camara_rate,
        timeout=settings.http_timeout,
        user_agent=settings.user_agent,
    ) as hc:
        dep_ids = await _list_ids_generic(hc, "/deputados", page_size=page_size)

        async def dep_worker(dep_id: str):
            async def fetch_rel(suffix: str) -> list[dict]:
                return await camara_fetch(
                    hc, f"/deputados/{dep_id}/{suffix}", {},
                    itens=page_size, concurrency=8, fallback_follow_next=True,
                )

            dados_orgaos = await fetch_rel("orgaos")
            dados_histor = await fetch_rel("historico")
            dados_frentes = await fetch_rel("frentes")

            y_org = _bucket_year_for_items(dados_orgaos, years, default_bucket)
            y_hist = _bucket_year_for_items(dados_histor, years, default_bucket)
            y_frnt = _bucket_year_for_items(dados_frentes, years, default_bucket)

            def row(rel: str, y: int, data: list[dict]) -> dict[str, Any]:
                return {
                    "source": "camara",
                    "entity": rel,      # e.g., "deputados/orgaos"
                    "year": y,
                    "id": dep_id,
                    "url": f"{CAMARA_BASE}/deputados/{dep_id}/{rel.split('/', 1)[1]}",
                    "payload_json": json.dumps(
                        {"dados": data}, ensure_ascii=False, separators=(",", ":"), sort_keys=True
                    ),
                }

            return (
                row("deputados/orgaos", y_org, dados_orgaos),
                row("deputados/historico", y_hist, dados_histor),
                row("deputados/frentes", y_frnt, dados_frentes),
            )

        results, errs = await bounded_gather(dep_ids, dep_worker, concurrency=concurrency_deputados)
        if errs:
            log.warning(f"[camara:deputados→relations] errors={len(errs)}")

    # Group by (relation, year) to write deterministic part sets
    by_rel_year: dict[tuple[str, int], list[dict[str, Any]]] = {}
    for triple in results:
        for row in triple:
            key = (row["entity"], int(row["year"]))
            by_rel_year.setdefault(key, []).append(row)

    for (rel, y), rows in sorted(by_rel_year.items(), key=lambda x: (x[0][0], x[0][1])):
        parts = write_relation_parts(
            rows,
            paths=paths,
            manifest=manifest,
            source="camara",
            relation=rel,   # e.g., "deputados/orgaos"
            year=y,
            part_rows=50_000,
            sort=True,
        )
        if rel == "deputados/orgaos":
            tot_orgs += len(rows)
        elif rel == "deputados/historico":
            tot_hist += len(rows)
        elif rel == "deputados/frentes":
            tot_frentes += len(rows)
        log.info(f"[camara:{rel}] year={y} wrote {len(rows)} rows in {len(parts)} part(s)")

    log.info(f"[camara:deputados relations] orgaos={tot_orgs} historico={tot_hist} frentes={tot_frentes}")
    return tot_orgs, tot_hist, tot_frentes


# ---- 6) PARTIDOS / BLOCOS / FRENTES / LEGISLATURAS --------------------------

async def build_partidos_blocos_frentes_legislaturas(
    paths: BronzePaths,
    manifest: SnapshotManifest,
    years: Iterable[int],
    *,
    page_size: int = 100,
    list_concurrency: int = 8,
    fetch_concurrency: int = 16,
    concurrency_rel: int = 16,
    year_bucket: int = 0,  # catálogos estáticos
) -> tuple[int, int]:
    """
    - Catálogos (detalhes) em year=0000:
        * /partidos, /blocos, /frentes, /legislaturas  -> GET {id}
    - Relações com variação temporal → bucket pelo 1º avistamento no intervalo:
        * partidos/{id}/membros, partidos/{id}/lideres
        * blocos/{id}/partidos
        * frentes/{id}/membros
        * legislaturas/{id}/lideres, legislaturas/{id}/mesa

    Returns (num_detail_rows, num_relation_rows)
    """
    setup_logging()
    details_written = 0
    relations_written = 0
    y0 = min(years) if years else 0
    default_bucket = y0

    async with HttpClient(
        CAMARA_BASE,
        rate_per_sec=settings.camara_rate,
        timeout=settings.http_timeout,
        user_agent=settings.user_agent,
    ) as hc:

        async def write_details(entity_name: str, base: str, id_fields: tuple[str, ...] = ("id",)):
            ids = await _list_ids_generic(
                hc, f"/{base}", page_size=page_size,
                id_fields=id_fields,
                extra_params={"idLegislatura": ",".join(leg_ids)} if base == "frentes" and leg_ids else None,
                supports_ordering=(base != "frentes"),
            )

            async def worker(eid: str) -> dict[str, Any]:
                url = f"/{base}/{eid}"
                dados = await camara_fetch(
                    hc, url, {},
                    itens=100, concurrency=8, fallback_follow_next=True
                )
                return {
                    "source": "camara",
                    "entity": entity_name,
                    "year": year_bucket,
                    "id": eid,
                    "url": CAMARA_BASE + url,
                    "payload_json": json.dumps(
                        {"dados": dados}, ensure_ascii=False, separators=(",", ":"), sort_keys=True
                    ),
                }

            rows, errs = await bounded_gather(ids, worker, concurrency=fetch_concurrency)
            if errs:
                log.warning(f"[camara:{base}(all)] detail_errors={len(errs)}")
            parts = write_details_parts(
                rows,
                paths=paths,
                manifest=manifest,
                source="camara",
                entity=entity_name,
                year=year_bucket,
                part_rows=50_000,
                sort=True,
            )
            log.info(f"[camara:{base}(all)] wrote {len(rows)} rows in {len(parts)} part(s) → year={year_bucket:04d}")
            return len(rows), ids

        # ---- Details catalogs (year=0000) ----
        n_part, part_ids = await write_details("partidos", "partidos")
        n_bloc, bloc_ids = await write_details("blocos", "blocos")
        leg_ids = await _legislaturas_for_years(hc, years)
        n_frnt, frnt_ids = await write_details(
            "frentes", "frentes",
            ("id", "idFrente"),
            # pass params and skip ordering
        )
        n_leg, leg_ids = await write_details("legislaturas", "legislaturas")
        details_written = n_part + n_bloc + n_frnt + n_leg

        # ---- Relations (bucket by first-seen-in-interval) ----
        by_rel_year: dict[tuple[str, int], list[dict[str, Any]]] = {}

        async def add_relations_for_ids(base: str, ids: list[str], rels: list[str]):
            async def rel_worker(eid: str):
                out_rows: list[dict[str, Any]] = []
                for rel_suffix in rels:
                    dados = await camara_fetch(
                        hc, f"/{base}/{eid}/{rel_suffix}", {},
                        itens=page_size, concurrency=8, fallback_follow_next=True,
                    )
                    y = _bucket_year_for_items(dados, years, default_bucket)
                    rel_full = f"{base}/{rel_suffix}"
                    row = {
                        "source": "camara",
                        "entity": rel_full,
                        "year": y,
                        "id": eid,
                        "url": f"{CAMARA_BASE}/{base}/{eid}/{rel_suffix}",
                        "payload_json": json.dumps(
                            {"dados": dados}, ensure_ascii=False, separators=(",", ":"), sort_keys=True
                        ),
                    }
                    out_rows.append(row)
                return out_rows

            results, errs = await bounded_gather(ids, rel_worker, concurrency=concurrency_rel)
            if errs:
                log.warning(f"[camara:{base} relations] errors={len(errs)}")
            for rows in results:
                for row in rows:
                    key = (row["entity"], int(row["year"]))
                    by_rel_year.setdefault(key, []).append(row)

        # partidos: membros, lideres
        await add_relations_for_ids("partidos", part_ids, ["membros", "lideres"])
        # blocos: partidos
        await add_relations_for_ids("blocos",   bloc_ids, ["partidos"])
        # frentes: membros
        await add_relations_for_ids("frentes",  frnt_ids, ["membros"])
        # legislaturas: lideres, mesa
        await add_relations_for_ids("legislaturas", leg_ids, ["lideres", "mesa"])

    # write grouped relations
    for (rel, y), rows in sorted(by_rel_year.items(), key=lambda x: (x[0][0], x[0][1])):
        parts = write_relation_parts(
            rows,
            paths=paths,
            manifest=manifest,
            source="camara",
            relation=rel,  # e.g., "partidos/membros"
            year=y,
            part_rows=50_000,
            sort=True,
        )
        relations_written += len(rows)
        log.info(f"[camara:{rel}] year={y} wrote {len(rows)} rows in {len(parts)} part(s)")

    log.info(f"[camara:partidos+blocos+frentes+legislaturas] details={details_written} relations={relations_written}")
    return details_written, relations_written


async def _legislaturas_for_years(hc: HttpClient, years: Iterable[int]) -> list[str]:
    y0, y1 = min(years), max(years)
    dados = await camara_fetch(hc, "/legislaturas", {}, itens=100, concurrency=8, fallback_follow_next=True)
    out: list[str] = []
    for it in dados or []:
        try:
            lid = str(int(it.get("id")))
        except Exception:
            continue
        di = (it.get("dataInicio") or "")[:10]
        df = (it.get("dataFim") or "")[:10]
        try:
            yi = int(di[:4]); yf = int(df[:4]) if df else yi
        except Exception:
            continue
        if not (yf < y0 or yi > y1):
            out.append(lid)
    return sorted(set(out), key=int)
