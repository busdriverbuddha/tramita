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
from tramita.sources.camara.client import camara_fetch_all_dados
from tramita.storage.manifest import SnapshotManifest
from tramita.storage.parquet import write_index_parquet, write_details_parts, write_relation_parts
from tramita.storage.paths import BronzePaths

log = logging.getLogger(__name__)


CAMARA_BASE = settings.camara_base_url.rstrip("/")
_DEP_RE = re.compile(r"/deputados/(\d+)")
_ORG_RE = re.compile(r"/orgaos/(\d+)")


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
        dados = await camara_fetch_all_dados(
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
        })

    n = write_index_parquet(rows, idx_path)
    log.info(f"[camara:index] year={year} proposicoes={n} -> {idx_path}")
    return n


async def _fetch_detail(hc: HttpClient, year: int, rec: dict) -> dict:
    pid = str(rec["id"])
    # Prefer the provided URL; fallback to canonical
    url = rec.get("url") or f"{CAMARA_BASE}/proposicoes/{pid}"
    text = await hc.get_text(url)
    # Keep raw JSON text; we also pass 'year' so the writer can sort
    return {
        "source": "camara",
        "entity": "proposicoes",
        "year": year,
        "id": pid,
        "url": url,
        "payload_json": text,
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
    idx_path = paths.index_file("camara", "proposicoes", year)
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
        # you can also append to paths.failed_ids_csv here if you like
        log.warning(
            f"[camara:details] year={year} errors={len(errs)} (will still write successful rows)")

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
    n_rows = sum(p.num_rows for p in []) if False else len(rows)
    log.info(
        f"[camara:details] year={year} wrote {n_rows} rows in {len(parts)} part(s)")
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
                    dados = await camara_fetch_all_dados(
                        hc, "/proposicoes", params,
                        itens=page_size, concurrency=8, fallback_follow_next=True,
                    )
                    all_rows.extend(dados)
            else:
                dados = await camara_fetch_all_dados(
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
                txt = await hc.get_text(path)
                try:
                    obj = json.loads(txt)
                    dados = obj.get("dados") if isinstance(obj, dict) else obj
                    if dados is None:
                        # fall back to raw obj if schema differs
                        dados = obj
                except Exception as e:
                    raise RuntimeError(f"{pid} {relation} JSON decode error: {e}") from e

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
                txt = await hc.get_text(path)
                try:
                    obj = json.loads(txt)
                    dados = obj.get("dados") or []
                except Exception as e:
                    raise RuntimeError(f"{pid} autores JSON decode error: {e}") from e

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
            txt = await hc.get_text(url)
            return {
                "source": "camara",
                "entity": "deputados",
                "year": yy,
                "id": dep_id,
                "url": CAMARA_BASE + url,
                "payload_json": txt,
            }

        async def org_worker(yy: int, org_id: str):
            url = f"/orgaos/{org_id}"
            txt = await hc.get_text(url)
            return {
                "source": "camara",
                "entity": "orgaos",
                "year": yy,
                "id": org_id,
                "url": CAMARA_BASE + url,
                "payload_json": txt,
            }

        # Deputados
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
            txt = await hc.get_text(path)
            try:
                obj = json.loads(txt)
                dados = obj.get("dados") or []
            except Exception as e:
                raise RuntimeError(f"{pid} relacionadas JSON decode error: {e}") from e

            # Collect new proposicao ids from 'dados'
            new_ids: list[str] = []
            for it in dados:
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
