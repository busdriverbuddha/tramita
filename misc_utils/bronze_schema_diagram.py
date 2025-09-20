from __future__ import annotations

# Bronze Schema Diagram Generator
# Usage:
#   python bronze_schema_diagram.py /path/to/bronze/snapshots/bronze-2020-2024-v1 --out ./schema_out
#
# Outputs (in --out):
#   - bronze_schema.md   (Markdown report with Mermaid ER diagram + columns)
#   - bronze_schema.mmd  (Mermaid ER diagram only)
#   - bronze_schema.json (Machine-readable schema summary)
#
# Requirements:
#   pip install pyarrow
#
# Notes:
#   - Relationships are inferred heuristically by shared "*_id" or "codigo*" columns.
#   - You can paste the Mermaid block from the Markdown back into ChatGPT for discussion.

import json
import os
import re
from pathlib import Path
from dataclasses import dataclass, field
from typing import Sequence
from datetime import datetime

import pyarrow.parquet as pq
import pyarrow as pa


@dataclass
class ColumnInfo:
    name: str
    pa_type: str
    nullable: bool


@dataclass
class DatasetInfo:
    name: str           # e.g., "camara/proposicoes/details/year=2020"
    table: str          # node/table name for ERD, e.g., "camara_proposicoes_details"
    path: Path
    columns: list[ColumnInfo] = field(default_factory=list)


def _normalize_table_name(parts: Sequence[str]) -> str:
    safe = "_".join([re.sub(r"[^A-Za-z0-9]+", "_", p) for p in parts if p])
    safe = re.sub(r"_+", "_", safe).strip("_")
    if re.match(r"^\\d", safe):
        safe = f"t_{safe}"
    return safe.lower()[:120]


def _leaf_parquet(path: Path) -> Path | None:
    if path.is_file() and path.suffix == ".parquet":
        return path
    if not path.exists():
        return None
    files = list(path.glob("*.parquet"))
    if files:
        return sorted(files)[0]
    for child in sorted(path.iterdir()):
        if child.is_dir():
            files = list(child.glob("*.parquet"))
            if files:
                return sorted(files)[0]
    return None


def _arrow_schema_for(path: Path) -> pa.schema | None:
    try:
        pf = pq.ParquetFile(path)
        return pf.schema_arrow
    except Exception:
        return None


def _collect_datasets(root: Path) -> list[DatasetInfo]:
    datasets: list[DatasetInfo] = []
    for dirpath, dirnames, filenames in os.walk(root):
        p = Path(dirpath)
        if any(part.startswith("_") for part in p.parts):
            continue
        candidate = _leaf_parquet(p)
        if candidate:
            rel = Path(dirpath).relative_to(root)
            parts = [x for x in rel.parts if "=" not in x]
            table = _normalize_table_name(parts)
            ds = DatasetInfo(name=str(rel), table=table, path=candidate)
            sch = _arrow_schema_for(candidate)
            if sch is not None:
                cols: list[ColumnInfo] = []
                for f in sch:
                    cols.append(ColumnInfo(name=f.name, pa_type=str(f.type), nullable=f.nullable))
                ds.columns = cols
            datasets.append(ds)
    seen: set[str] = set()
    uniq: list[DatasetInfo] = []
    for ds in sorted(datasets, key=lambda d: d.name):
        if ds.table not in seen:
            uniq.append(ds)
            seen.add(ds.table)
    return uniq


def _guess_pk(cols: list[ColumnInfo]) -> str | None:
    candidates = [
        "id", "id_proposicao", "id_processo", "id_materia", "id_votacao",
        "codigo", "codigoMateria", "codigoVotacao", "codigoSessao",
        "codigoProposicao", "codigoEvento", "codigoOrgao", "codigoSessaoVotacao"
    ]
    names = {c.name.lower() for c in cols}
    for c in candidates:
        if c.lower() in names:
            return c
    for c in cols:
        if c.name.lower().endswith("_id"):
            return c.name
    return None


def _shared_key(a: DatasetInfo, b: DatasetInfo) -> str | None:
    a_names = {c.name for c in a.columns}
    b_names = {c.name for c in b.columns}
    intersection = a_names & b_names
    for n in sorted(intersection):
        if n.lower().endswith("_id") or n.lower().startswith("codigo"):
            return n
    a_pk = _guess_pk(a.columns)
    if a_pk and a_pk in b_names:
        return a_pk
    b_pk = _guess_pk(b.columns)
    if b_pk and b_pk in a_names:
        return b_pk
    return None


def _mermaid_type(t: str) -> str:
    t = t.lower()
    if any(k in t for k in ("int", "long", "decimal")):
        return "int"
    if "bool" in t:
        return "bool"
    if any(k in t for k in ("date", "time", "timestamp")):
        return "datetime"
    if any(k in t for k in ("float", "double", "real")):
        return "float"
    return "string"


def build_mermaid(datasets: list[DatasetInfo]) -> str:
    lines: list[str] = ["erDiagram"]
    for ds in datasets:
        lines.append(f"  {ds.table} {{")
        pk = _guess_pk(ds.columns)
        for col in ds.columns:
            t = _mermaid_type(col.pa_type)
            suffix = " PK" if pk and col.name == pk else ""
            lines.append(f"    {t} {col.name}{suffix}")
        lines.append("  }")
    for i, a in enumerate(datasets):
        for b in datasets[i+1:]:
            key = _shared_key(a, b)
            if not key:
                continue
            a_pk = _guess_pk(a.columns)
            b_pk = _guess_pk(b.columns)
            if b_pk and key == b_pk:
                rel = f'  {a.table} }}o--|| {b.table} : "{key}"'
            elif a_pk and key == a_pk:
                rel = f'  {b.table} }}o--|| {a.table} : "{key}"'
            else:
                rel = f'  {a.table} }}o--o{{ {b.table} : "{key}"'
            lines.append(rel)
    return "\n".join(lines)


def build_markdown(datasets: list[DatasetInfo], mermaid: str, root: Path) -> str:
    ts = datetime.now().isoformat(timespec="seconds")
    md: list[str] = []
    md.append(f"# Bronze Schema Report\\n\\nGenerated: {ts}\\n\\nRoot: `{root}`\\n")
    md.append("## ER Diagram (Mermaid)\\n")
    md.append("```mermaid")
    md.append(mermaid)
    md.append("```\\n")
    md.append("## Datasets & Columns\\n")
    for ds in datasets:
        md.append(f"### {ds.table}\\n")
        md.append(f"_Source_: `{ds.name}`\\n")
        if not ds.columns:
            md.append("> (No columns detected — unreadable or empty Parquet)\\n")
            continue
        md.append("| Column | Type (Arrow) | Nullable |")
        md.append("|---|---|---|")
        for c in ds.columns:
            md.append(f"| `{c.name}` | `{c.pa_type}` | `{c.nullable}` |")
        md.append("")
    return "\\n".join(md)


def generate(root_str: str, out_dir: str = ".") -> dict:
    root = Path(root_str).resolve()
    out = Path(out_dir).resolve()
    out.mkdir(parents=True, exist_ok=True)
    datasets = _collect_datasets(root)
    mermaid = build_mermaid(datasets)
    md = build_markdown(datasets, mermaid, root)
    schema_json = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "root": str(root),
        "datasets": [
            {
                "name": ds.name,
                "table": ds.table,
                "path": str(ds.path),
                "columns": [{"name": c.name, "pa_type": c.pa_type, "nullable": c.nullable} for c in ds.columns],
            }
            for ds in datasets
        ],
    }
    json_path = out / "bronze_schema.json"
    md_path = out / "bronze_schema.md"
    mermaid_path = out / "bronze_schema.mmd"
    mermaid_path.write_text(mermaid, encoding="utf-8")
    md_path.write_text(md, encoding="utf-8")
    json_path.write_text(json.dumps(schema_json, indent=2, ensure_ascii=False), encoding="utf-8")
    return {"json": str(json_path), "markdown": str(md_path), "mermaid": str(mermaid_path), "tables": len(datasets)}


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser(description="Generate Mermaid ERD and Markdown schema from a Bronze Parquet snapshot.")
    ap.add_argument("root", help="Path to the Bronze snapshot (e.g., ./bronze/snapshots/bronze-2020-2024-v1)")
    ap.add_argument("--out", default=".", help="Output directory (default: current dir)")
    args = ap.parse_args()
    result = generate(args.root, args.out)
    print(json.dumps(result, indent=2))
