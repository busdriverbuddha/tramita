# tramita/storage/parquet.py

from typing import Iterable, TypedDict, Any
from pathlib import Path
import json
import hashlib

import pyarrow as pa
import pyarrow.parquet as pq


from tramita.storage.paths import BronzePaths
from tramita.storage.manifest import SnapshotManifest


# ---- Bronze row shapes ------------------------------------------------------
class RawDetailRow(TypedDict):
    """
    Bronze 'details' (or relations) row.
    Keep it raw; parse later in Prata.
    """
    source: str          # "camara" | "senado"
    entity: str          # e.g., "proposicoes"
    year: int
    id: str              # treat as string to avoid surprises
    url: str
    payload_json: str    # exact JSON text as returned
    payload_sha256: str  # sha of payload_json


class IndexRow(TypedDict):
    """
    Bronze index row: minimal info to resume/downstream details.
    """
    source: str
    entity: str
    year: int
    id: str
    url: str


# ---- Helpers ----------------------------------------------------------------

def _sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _ensure_payload(row: dict[str, Any], *, year: int | None = None) -> RawDetailRow:
    """
    Coerce/validate a row into the RawDetailRow shape.
    - payload_json may arrive as dict -> serialize deterministically
    - id coerced to str
    """
    payload = row.get("payload_json")
    if isinstance(payload, (dict, list)):
        # Deterministic JSON (sorted keys, no whitespace differences)
        payload_json = json.dumps(payload, ensure_ascii=False, separators=(",", ":"), sort_keys=True)
    elif isinstance(payload, (bytes, bytearray)):
        payload_json = payload.decode("utf-8")
    elif isinstance(payload, str):
        # Keep as-is (already raw)
        payload_json = payload
    else:
        raise ValueError("payload_json missing or unsupported type")

    y = row.get("year", year)
    if y is None:
        raise ValueError("year is required for RawDetailRow")
    payload_sha256 = row.get("payload_sha256") or _sha256_text(payload_json)

    out: RawDetailRow = {
        "source": str(row["source"]),
        "entity": str(row["entity"]),
        "year": int(y),
        "id": str(row["id"]),
        "url": str(row["url"]),
        "payload_json": payload_json,
        "payload_sha256": str(payload_sha256),
    }
    return out


def _ensure_index(row: dict[str, Any], *, year: int | None = None) -> IndexRow:
    y = row.get("year", year)
    if y is None:
        raise ValueError("year is required for IndexRow")
    return {
        "source": str(row["source"]),
        "entity": str(row["entity"]),
        "year": int(y),                 # present in Python
        "id": str(row["id"]),
        "url": str(row["url"]),
    }


# ---- Parquet writing ---------------------------------------------------------

# Stable Arrow schema (order matters for parquet determinism)
DETAIL_SCHEMA = pa.schema([
    pa.field("source", pa.string()),
    pa.field("entity", pa.string()),
    pa.field("id", pa.string()),
    pa.field("url", pa.string()),
    pa.field("payload_json", pa.string()),
    pa.field("payload_sha256", pa.string()),
])

INDEX_SCHEMA = pa.schema([
    pa.field("source", pa.string()),
    pa.field("entity", pa.string()),
    pa.field("id", pa.string()),
    pa.field("url", pa.string()),
])


def _to_table(rows: list[dict], schema: pa.Schema) -> pa.Table:
    # pylist -> Table: preserves column order if keys match schema
    return pa.Table.from_pylist(rows, schema=schema)


def _write_table(path: Path, table: pa.Table) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    # Compression + dictionary encoding for compactness; deterministic defaults
    pq.write_table(
        table, path,
        compression="zstd",
        use_dictionary=True,
        data_page_size=1024 * 1024,  # 1MB pages (fine default; stable)
        write_statistics=True,
    )


# ---- Public API --------------------------------------------------------------
def write_index_parquet(
    rows: Iterable[dict[str, Any]],
    out_path: Path,
    *,
    sort_keys: tuple[str, ...] = ("year", "id"),
) -> int:
    buf: list[IndexRow] = [_ensure_index(r) for r in rows]
    buf.sort(key=lambda x: tuple(str(x[k]).zfill(4) if isinstance(x[k], int) else str(x[k]) for k in sort_keys))
    table = pa.Table.from_pylist([{k: v for k, v in r.items() if k in {f.name for f in INDEX_SCHEMA}} for r in buf],
                                 schema=INDEX_SCHEMA)
    _write_table(out_path, table)
    return len(buf)


def write_details_parts(
    rows: Iterable[dict[str, Any]],
    *,
    paths: BronzePaths,
    manifest: SnapshotManifest,
    source: str,
    entity: str,
    year: int,
    part_rows: int = 50_000,
    sort: bool = True,
) -> list[Path]:
    normalized: list[RawDetailRow] = [_ensure_payload(r, year=year) for r in rows]

    if sort:
        def sort_key(x: RawDetailRow):
            y = str(x["year"]).zfill(4)
            try:
                idx_key = str(int(x["id"])).zfill(12)
            except Exception:
                idx_key = str(x["id"])
            return (y, idx_key)
        normalized.sort(key=sort_key)

    part_dir = paths.details_part_dir(source, entity, year)
    written: list[Path] = []
    total = len(normalized)
    if total == 0:
        part_dir.mkdir(parents=True, exist_ok=True)
        return written

    start = 0
    part_idx = 0
    while start < total:
        end = min(start + part_rows, total)
        chunk = normalized[start:end]
        # project rows to Parquet schema (drop 'year' before writing)
        chunk_proj = [{k: v for k, v in r.items() if k in {f.name for f in DETAIL_SCHEMA}} for r in chunk]
        part_path = paths.details_part_file(source, entity, year, part_idx)
        table = pa.Table.from_pylist(chunk_proj, schema=DETAIL_SCHEMA)
        _write_table(part_path, table)
        manifest.add_file(paths.root, source=source, entity=entity, year=year, file_path=part_path, rows=len(chunk))
        written.append(part_path)
        start = end
        part_idx += 1

    return written


def write_relation_parts(
    rows: Iterable[dict[str, Any]],
    *,
    paths: BronzePaths,
    manifest: SnapshotManifest,
    source: str,
    relation: str,   # "tramitacoes" | "autores" | "votacoes" | ...
    year: int,
    part_rows: int = 50_000,
    sort: bool = True,
) -> list[Path]:
    """
    Same as details, but groups all rows of a relation under .../<relation>/year=YYYY/
    Useful when the per-proposição fan-out is large.
    """
    normalized: list[RawDetailRow] = [_ensure_payload(r, year=year) for r in rows]
    if sort:
        def sort_key(x: RawDetailRow):
            y = str(x["year"]).zfill(4)
            try:
                idx_key = str(int(x["id"])).zfill(12)
            except Exception:
                idx_key = str(x["id"])
            return (y, idx_key)
        normalized.sort(key=sort_key)

    written: list[Path] = []
    total = len(normalized)
    part_dir = paths.relation_part_dir(source, relation, year)
    part_dir.mkdir(parents=True, exist_ok=True)

    if total == 0:
        return written

    start = 0
    part_idx = 0
    while start < total:
        end = min(start + part_rows, total)
        chunk = normalized[start:end]
        chunk_proj = [{k: v for k, v in r.items() if k in {f.name for f in DETAIL_SCHEMA}} for r in chunk]
        part_path = paths.relation_part_file(source, relation, year, part_idx)
        table = pa.Table.from_pylist(chunk_proj, schema=DETAIL_SCHEMA)
        _write_table(part_path, table)
        manifest.add_file(paths.root, source=source, entity=relation, year=year, file_path=part_path, rows=len(chunk))
        written.append(part_path)
        start = end
        part_idx += 1

    return written
