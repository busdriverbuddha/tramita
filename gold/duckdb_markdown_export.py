#!/usr/bin/env python3
"""
duckdb_markdown_export.py

Export (1) schemas and (2) samples for all BASE TABLES in a DuckDB database as Markdown.

Usage:
  python duckdb_markdown_export.py path/to/db.duckdb \
      --out-schemas duckdb_schemas.md \
      --out-samples duckdb_samples.md \
      --limit 10
"""
from __future__ import annotations

import argparse
import datetime as dt
import pathlib
import sys
from typing import Any

import duckdb


def quote_ident(name: str) -> str:
    """Double-quote an identifier, escaping embedded quotes."""
    return '"' + name.replace('"', '""') + '"'


def fqtn(schema: str, table: str) -> str:
    """Fully-qualified table name with proper quoting."""
    return f'{quote_ident(schema)}.{quote_ident(table)}'


def get_tables(conn: duckdb.DuckDBPyConnection) -> list[tuple[str, str]]:
    """
    Return [(schema, table)] for all base tables (exclude system schemas).
    """
    rows = conn.execute(
        """
        select table_schema, table_name
        from information_schema.tables
        where table_type = 'BASE TABLE'
          and table_schema not in ('information_schema', 'pg_catalog')
        order by table_schema, table_name
        """
    ).fetchall()
    return [(r[0], r[1]) for r in rows]


def get_columns(conn: duckdb.DuckDBPyConnection, schema: str, table: str) -> list[dict[str, Any]]:
    """
    Return column metadata (name, data_type, is_nullable, ordinal_position, character_maximum_length).
    """
    rows = conn.execute(
        """
        select
            column_name,
            data_type,
            is_nullable,
            ordinal_position,
            character_maximum_length
        from information_schema.columns
        where table_schema = ? and table_name = ?
        order by ordinal_position
        """,
        [schema, table],
    ).fetchall()

    cols: list[dict[str, Any]] = []
    for name, dtype, isnull, pos, charlen in rows:
        cols.append(
            {
                "column_name": name,
                "data_type": dtype,
                "is_nullable": (str(isnull).upper() == "YES"),
                "ordinal_position": pos,
                "character_maximum_length": charlen,
            }
        )
    return cols


def get_primary_key_columns(conn: duckdb.DuckDBPyConnection, schema: str, table: str) -> list[str]:
    """
    Best-effort PK detection via information_schema. If not present, returns [].

    DuckDB exposes primary keys via:
      - information_schema.table_constraints
      - information_schema.key_column_usage
    """
    rows = conn.execute(
        """
        with pk as (
            select constraint_name
            from information_schema.table_constraints
            where table_schema = ? and table_name = ? and constraint_type = 'PRIMARY KEY'
        )
        select k.column_name
        from information_schema.key_column_usage k
        join pk on k.constraint_name = pk.constraint_name
        where k.table_schema = ? and k.table_name = ?
        order by k.ordinal_position
        """,
        [schema, table, schema, table],
    ).fetchall()
    return [r[0] for r in rows]


def render_create_markdown(schema: str, table: str, cols: list[dict[str, Any]], pk_cols: list[str]) -> str:
    """
    Render a CREATE TABLE-like block for Markdown (SQL fenced code block),
    followed by a compact column table.
    """
    # Build CREATE-like definition
    lines: list[str] = []
    lines.append(f'CREATE TABLE {quote_ident(table)} (')
    col_lines: list[str] = []
    for c in cols:
        dtype = c["data_type"]
        # If DuckDB reported a character_maximum_length, append (N) for readability
        if c["character_maximum_length"] and "CHAR" in dtype.upper():
            dtype = f'{dtype}({c["character_maximum_length"]})'
        nn = "" if c["is_nullable"] else " NOT NULL"
        col_lines.append(f'  {quote_ident(c["column_name"])} {dtype}{nn}')
    if pk_cols:
        pk = ", ".join(quote_ident(x) for x in pk_cols)
        col_lines.append(f'  PRIMARY KEY ({pk})')
    lines.append(",\n".join(col_lines))
    lines.append(");")

    # Column overview as Markdown table
    md_table = to_markdown_table(
        headers=["column_name", "data_type", "nullable", "ordinal_position"],
        rows=[
            [c["column_name"], c["data_type"], "YES" if c["is_nullable"] else "NO", c["ordinal_position"]]
            for c in cols
        ],
    )

    return (
        f"## {schema}.{table}\n\n"
        f"**Create statement:**\n\n```sql\n" + "\n".join(lines) + "\n```\n\n"
        f"**Columns:**\n\n{md_table}\n"
    )


def escape_md(v: Any) -> str:
    """
    Convert value to a Markdown-safe string.
    - Escapes pipe characters to avoid breaking tables.
    - Shows None as empty.
    - Shortens long strings for preview (sample), but keeps full content by default.
    """
    if v is None:
        return ""
    s = str(v)
    return s.replace("|", r"\|")


def to_markdown_table(headers: list[str], rows: list[list[Any]]) -> str:
    """
    Render a GitHub-style Markdown table from headers and row values.
    """
    h = "| " + " | ".join(escape_md(x) for x in headers) + " |"
    sep = "| " + " | ".join("---" for _ in headers) + " |"
    body_lines: list[str] = []
    for r in rows:
        body_lines.append("| " + " | ".join(escape_md(x) for x in r) + " |")
    body = "\n".join(body_lines) if body_lines else "_(no rows)_"
    return "\n".join([h, sep, body])


def sample_table(
    conn: duckdb.DuckDBPyConnection, schema: str, table: str, limit: int
) -> tuple[list[str], list[list[Any]]]:
    """
    Return (headers, rows) for a LIMIT sample from a table.
    """
    sql = f"select * from {fqtn(schema, table)} limit {int(limit)}"
    cur = conn.execute(sql)
    rows = cur.fetchall()
    headers = [d[0] for d in cur.description] if cur.description else []
    return headers, rows


def write_text(path: pathlib.Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def make_header(title: str) -> str:
    now = dt.datetime.now().isoformat(timespec="seconds")
    return f"# {title}\n\n_Generated on {now}_\n\n"


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Export DuckDB schemas and samples to Markdown.")
    parser.add_argument("database", help="Path to DuckDB database file (e.g., data.duckdb)")
    parser.add_argument("--out-schemas", default="duckdb_schemas.md", help="Output Markdown for schemas")
    parser.add_argument("--out-samples", default="duckdb_samples.md", help="Output Markdown for samples")
    parser.add_argument("--limit", type=int, default=10, help="Rows per table in the samples file")
    parser.add_argument("--read-only", action="store_true", help="Open DuckDB in read-only mode")
    args = parser.parse_args(argv)

    db_path = args.database
    out_schemas = pathlib.Path(args.out_schemas)
    out_samples = pathlib.Path(args.out_samples)

    # Connect
    conn = duckdb.connect(database=db_path, read_only=args.read_only)

    # Discover tables
    tables = get_tables(conn)
    if not tables:
        write_text(out_schemas, make_header("DuckDB Schemas") + "_No base tables found._\n")
        write_text(out_samples, make_header("DuckDB Samples") + "_No base tables found._\n")
        print("No base tables found.")
        return 0

    # Build schemas markdown
    schema_md_parts: list[str] = [make_header("DuckDB Schemas")]
    for schema, table in tables:
        cols = get_columns(conn, schema, table)
        pk_cols = get_primary_key_columns(conn, schema, table)
        schema_md_parts.append(render_create_markdown(schema, table, cols, pk_cols))
    write_text(out_schemas, "\n".join(schema_md_parts))

    # Build samples markdown
    sample_md_parts: list[str] = [make_header("DuckDB Samples")]
    for schema, table in tables:
        headers, rows = sample_table(conn, schema, table, limit=args.limit)
        sample_md_parts.append(f"## {schema}.{table}\n")
        sample_md_parts.append(f"_Query_: `SELECT * FROM {fqtn(schema, table)} LIMIT {args.limit};`\n")
        if headers:
            sample_md_parts.append(to_markdown_table(headers, rows))
        else:
            sample_md_parts.append("_(empty table or no columns)_")
        sample_md_parts.append("")  # extra newline
    write_text(out_samples, "\n".join(sample_md_parts))

    print(f"Wrote:\n  - Schemas: {out_schemas}\n  - Samples: {out_samples}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
