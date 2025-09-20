import os, sys
from typing import Iterable
import pyarrow as pa
import pyarrow.dataset as ds
import pyarrow.compute as pc

ROOT = "data/bronze/snapshots/bronze-2020-smoke/senado"

TARGETS: dict[str, list[str]] = {
    "bloco": ["bloco/details"],
    "bloco_partido": ["bloco_partido"],
    "colegiado": ["colegiado/details"],
    "emendas": ["emendas"],
    "parlamentar_details": ["parlamentar/details"],
    "parlamentar_index": ["parlamentar/index"],
    "partido": ["partido/details"],
    "processo_details": ["processo/details"],
    "processo_index": ["processo/index"],
    "relatorias": ["relatorias"],
    "votacoes": ["votacoes"],
    "votacoes_colegiado": ["votacoes_colegiado"],
}

def _ds(path: str) -> ds.Dataset:
    return ds.dataset(path, format="parquet", partitioning="hive")

def _count_rows(dataset: ds.Dataset) -> int:
    if hasattr(dataset, "count_rows"):
        return dataset.count_rows()
    return dataset.to_table(columns=[]).num_rows

def _year_counts(dataset: ds.Dataset) -> pa.Table | None:
    try:
        tbl = dataset.to_table(columns=["year"])
        vc = pc.value_counts(tbl["year"])
        values = pc.struct_field(vc, "values")
        counts = pc.struct_field(vc, "counts")
        t = pa.table({"year": values, "count": counts})
        order = pc.sort_indices(t, sort_keys=[("year", "ascending")])
        return pc.take(t, order)  # Table with 'year', 'count'
    except Exception:
        return None

def _schema(dataset: ds.Dataset) -> pa.schema:
    return dataset.schema

# ---------- helpers that don't rely on scanner(limit=...) ----------
def _scan_limit(dataset: ds.Dataset, n: int, *, filter: ds.Expression | None = None, columns: list[str] | None = None) -> pa.Table:
    """Read up to n rows by iterating batches; works on older PyArrow."""
    scanner = ds.Scanner.from_dataset(dataset, filter=filter, columns=columns)
    remaining = n
    batches: list[pa.RecordBatch] = []
    for batch in scanner.to_batches():
        if remaining <= 0:
            break
        if len(batch) > remaining:
            batch = batch.slice(0, remaining)
        batches.append(batch)
        remaining -= len(batch)
    return pa.Table.from_batches(batches) if batches else pa.table({c: pa.array([], type=dataset.schema.field(c).type) for c in (columns or dataset.schema.names)})

def _head(dataset: ds.Dataset, n: int = 5) -> pa.Table:
    return _scan_limit(dataset, n)

def _sample_year(dataset: ds.Dataset, year: int, n: int = 5) -> pa.Table:
    return _scan_limit(dataset, n, filter=(ds.field("year") == year))

def _example_year(dataset: ds.Dataset) -> int | None:
    yc = _year_counts(dataset)
    if yc is None or len(yc) == 0:
        return None
    return int(pc.min(yc["year"]).as_py())

# -------------------------------------------------------------------

def _null_rates(table: pa.Table, cols: Iterable[str]) -> dict[str, float]:
    rates: dict[str, float] = {}
    for c in cols:
        if c not in table.column_names:
            continue
        col = table[c]
        rates[c] = 0.0 if col.null_count == 0 else float(col.null_count) / float(len(col))
    return rates

def _print_line(title: str) -> None:
    print("\n" + title)
    print("-" * len(title))

def inspect_path(abs_path: str) -> None:
    dset = _ds(abs_path)
    _print_line(f"Dataset: {abs_path}")

    # Schema
    sch = _schema(dset)
    print("Schema:")
    for f in sch:
        print(f"  - {f.name}: {f.type} {'(nullable)' if f.nullable else '(required)'}")

    # Counts
    total = _count_rows(dset)
    print(f"\nRows (total): {total}")

    yc = _year_counts(dset)
    if yc is not None:
        print("\nRows by year:")
        for i in range(len(yc)):
            y = yc["year"][i].as_py()
            c = yc["count"][i].as_py()
            print(f"  {y}: {c}")

    # Head
    print("\nHead (5 rows, any year):")
    try:
        head_tbl = _head(dset, 5)
        print(head_tbl.to_pandas().to_string(index=False) if len(head_tbl) else "  <empty>")
    except Exception as e:
        print(f"  <failed to preview head: {e}>")

    # Per-year small sample (first available year)
    y = _example_year(dset)
    if y is not None:
        print(f"\nSample rows for year={y}:")
        try:
            print(_sample_year(dset, y, 5).to_pandas().to_string(index=False))
        except Exception as e:
            print(f"  <failed to preview year sample: {e}>")

    # Basic null rates on likely keys
    likely_keys = ["id", "idBloco", "idPartido", "idColegiado", "idParlamentar",
                   "numero", "ano", "idProcesso", "idMateria", "idVotacao"]
    try:
        small = _scan_limit(dset, 10_000)
        rates = _null_rates(small, likely_keys)
        if rates:
            print("\nNull rates (sample of up to 10k rows):")
            for k, r in rates.items():
                print(f"  {k}: {r:.3f}")
    except Exception:
        pass

def main(which: list[str] | None = None) -> None:
    todo = {k: TARGETS[k] for k in which} if which else TARGETS
    for name, rels in todo.items():
        print("\n" + "=" * 80)
        print(f"Entity: {name}")
        print("=" * 80)
        for rel in rels:
            path = os.path.join(ROOT, rel)
            if not os.path.exists(path):
                print(f"[skip] {path} (not found)")
                continue
            inspect_path(path)

if __name__ == "__main__":
    args = sys.argv[1:]
    main(args if args else None)
