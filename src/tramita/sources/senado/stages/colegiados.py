# tramita/sources/senado/stages/colegiados.py

import json
import logging

from collections import defaultdict
from datetime import date, timedelta
from typing import Iterable

import pyarrow.parquet as pq

from tramita.config import settings
from tramita.http.client import HttpClient
from tramita.log import setup_logging
from tramita.sources.senado.client import senado_fetch, _dig
from tramita.storage.manifest import SnapshotManifest
from tramita.storage.parquet import write_details_parts, write_relation_parts
from tramita.storage.paths import BronzePaths
from tramita.sources.senado.utils import _slugify_natureza, _year_from

setup_logging()
log = logging.getLogger(__name__)

SENADO_BASE = settings.senado_base_url.rstrip("/")


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

    years_sorted = sorted(set(int(y) for y in years)) or []
    if not years_sorted:
        log.info("[senado:coleg_votos] no years requested; skipping")
        return 0

    # ---- 1) Discover committee SIGLAs from previously saved details
    siglas: set[str] = set()
    probe_dir = paths.details_part_dir("senado", "colegiado", years_sorted[0]).parent  # .../details
    if not probe_dir.exists():
        log.warning("[senado:coleg_votos] no colegiado details found at %s", probe_dir)
        return 0

    part_files = sorted(probe_dir.glob("year=*/part-*.parquet"))
    if not part_files:
        log.warning("[senado:coleg_votos] no colegiado parts found under %s", probe_dir)
        return 0

    for pf in part_files:
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
