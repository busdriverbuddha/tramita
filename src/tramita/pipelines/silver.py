"""
Silver (Prata) pipeline stubs.

This module defines the async entrypoint for the Câmara silver pipeline and a
simple synchronous wrapper to run it via asyncio. Implementation will be added
in a later step; for now, the function bodies are intentionally empty to keep
structure consistent with the bronze pipeline.
"""

from __future__ import annotations

import asyncio
import logging
import os
import json
import time
from datetime import datetime
from pathlib import Path
from typing import Iterable, Sequence
from glob import glob

import duckdb  # type: ignore

try:
    import pandas as pd  # type: ignore
except Exception:  # pragma: no cover - optional at runtime
    pd = None  # type: ignore

try:
    import pyarrow.parquet as pq  # type: ignore
except Exception:  # pragma: no cover - optional at runtime
    pq = None  # type: ignore


def _validate_duckdb_path_matches_snapshot(duckdb_path: str, snapshot: str) -> None:
    """Ensure the DuckDB path reflects the bronze snapshot signature.

    Policy: the duckdb path must contain the snapshot suffix portion (everything
    after the first hyphen), e.g., for snapshot "bronze-2020-2024-v2" the path
    should contain "2020-2024-v2" as a directory component or substring. A
    common layout looks like:

        ./data/silver/2020-2024-v2/duckdb/tramita_silver.duckdb

    Raises ValueError if the policy is not met.
    """
    # Extract signature ("2020-2024-v2" from "bronze-2020-2024-v2")
    sig = snapshot.split("-", 1)[1] if "-" in snapshot else snapshot
    p = str(duckdb_path)
    if sig not in p:
        raise ValueError(
            f"DuckDB path must reflect snapshot signature '{sig}': got '{duckdb_path}'"
        )


def _snapshot_signature(snapshot: str) -> str:
    """Extract signature string from snapshot name.

    Example: "bronze-2020-2024-v2" -> "2020-2024-v2".
    If no hyphen exists, returns the snapshot unchanged.
    """
    return snapshot.split("-", 1)[1] if "-" in snapshot else snapshot


def _ensure_within(base: Path, target: Path) -> None:
    """Ensure target path is within base path; raise ValueError otherwise."""
    try:
        target.resolve().relative_to(base.resolve())
    except Exception:
        raise ValueError(f"Steps directory must be within data_root: {target} not under {base}")


def _resolve_steps_dir(
    source: str,
    data_root: str | os.PathLike[str],
    snapshot: str,
    steps_dir: str | os.PathLike[str] | None,
) -> Path:
    data_root_p = Path(data_root)
    if steps_dir:
        p = Path(steps_dir)
        if not p.is_absolute():
            p = (data_root_p / p).resolve()
        _ensure_within(data_root_p, p)
        return p
    sig = _snapshot_signature(snapshot)
    # default locations under data_root for the given source
    candidates = [
        data_root_p / "silver" / "pipelines" / source / sig,
        data_root_p / "silver" / "pipelines" / source,
    ]
    for c in candidates:
        if c.exists():
            return c.resolve()
    # Default to the most specific path even if missing, to give a clear message upstream
    return (data_root_p / "silver" / "pipelines" / source / sig).resolve()


def _discover_steps(steps_root: Path) -> tuple[Path | None, Path | None, list[Path]]:
    """Return (prelude, macros, steps[]) from a steps root.

    - prelude: steps_root/prelude.py if present
    - macros:  steps_root/macros.sql if present
    - steps:   lexicographic .sql/.py from steps_root/steps if exists else steps_root,
               excluding prelude/macros files.
    """
    prelude = steps_root / "prelude.py"
    macros = steps_root / "macros.sql"
    prelude_path = prelude if prelude.exists() else None
    macros_path = macros if macros.exists() else None

    search_dir = steps_root / "steps" if (steps_root / "steps").exists() else steps_root
    all_files = [
        p for p in sorted(search_dir.iterdir())
        if p.is_file() and p.suffix in {".sql", ".py"}
    ]
    excluded = {prelude.resolve() if prelude_path else None, macros.resolve() if macros_path else None}
    excluded = {x for x in excluded if x is not None}
    steps = [p for p in all_files if p.resolve() not in excluded]
    return prelude_path, macros_path, steps


def _strip_sql_magics(text: str) -> str:
    lines = text.splitlines()
    out = []
    for ln in lines:
        if ln.lstrip().startswith("%%sql"):
            continue
        out.append(ln)
    return "\n".join(out)


def _subst_vars(text: str, mapping: dict[str, str]) -> str:
    out = text
    for k, v in mapping.items():
        out = out.replace(f"${{{k}}}", v)
    return out


def _split_sql_statements(text: str) -> list[str]:
    """Split SQL into statements on semicolons not inside quotes or comments.
    A lightweight splitter to avoid external deps; not a full SQL parser.
    """
    stmts: list[str] = []
    buf: list[str] = []
    in_squote = False
    in_dquote = False
    in_line_comment = False
    in_block_comment = False
    i = 0
    while i < len(text):
        ch = text[i]
        nxt = text[i + 1] if i + 1 < len(text) else ""
        if in_line_comment:
            if ch == "\n":
                in_line_comment = False
            buf.append(ch)
            i += 1
            continue
        if in_block_comment:
            if ch == "*" and nxt == "/":
                in_block_comment = False
                buf.append(ch)
                buf.append(nxt)
                i += 2
                continue
            buf.append(ch)
            i += 1
            continue
        # comment starts
        if ch == "-" and nxt == "-" and not in_squote and not in_dquote:
            in_line_comment = True
            buf.append(ch)
            buf.append(nxt)
            i += 2
            continue
        if ch == "/" and nxt == "*" and not in_squote and not in_dquote:
            in_block_comment = True
            buf.append(ch)
            buf.append(nxt)
            i += 2
            continue
        # quotes
        if ch == "'" and not in_dquote:
            in_squote = not in_squote
            buf.append(ch)
            i += 1
            continue
        if ch == '"' and not in_squote:
            in_dquote = not in_dquote
            buf.append(ch)
            i += 1
            continue
        # statement split
        if ch == ";" and not in_squote and not in_dquote:
            s = "".join(buf).strip()
            if s:
                stmts.append(s)
            buf = []
            i += 1
            continue
        buf.append(ch)
        i += 1
    s = "".join(buf).strip()
    if s:
        stmts.append(s)
    return stmts


async def _run_silver_source(
    source: str,
    snapshot: str,
    data_root: str = "./data",
    duckdb_path: str | os.PathLike[str] | None = None,
    steps_dir: str | os.PathLike[str] | None = None,
    dry_run: bool = False,
) -> None:
    """Async Silver pipeline entrypoint for a single source.

    Parameters
    - snapshot: Name of the bronze snapshot directory (e.g., "bronze-2020-2024-v2").
    - data_root: Root directory for data files (default: "./data").
    - duckdb_path: Target DuckDB file path; must include snapshot signature (e.g.,
      ./data/silver/2020-2024-v2/duckdb/tramita_silver.duckdb). If None, execution is limited.
    - steps_dir: Directory under data_root with user-supplied steps (.sql/.py). If not
      provided, defaults are used based on snapshot signature.
    - dry_run: If True, only list discovered steps and exit without execution.
    """
    log = logging.getLogger(f"tramita.silver.{source}")

    # Enforce duckdb path policy if provided
    if duckdb_path is not None:
        _validate_duckdb_path_matches_snapshot(str(duckdb_path), snapshot)

    # Resolve steps directory (must be under data_root)
    steps_root = _resolve_steps_dir(source, data_root, snapshot, steps_dir)
    _ensure_within(Path(data_root), steps_root)
    if not steps_root.exists():
        raise FileNotFoundError(
            f"Steps directory not found: {steps_root} (under data_root={data_root})"
        )

    prelude, macros, steps = _discover_steps(steps_root)
    if not any([prelude, macros]) and not steps:
        raise FileNotFoundError(
            f"No step files (.sql/.py) found in {steps_root}"
        )

    if dry_run:
        sig = _snapshot_signature(snapshot)
        plan_lines: list[str] = []
        plan_lines.append(f"Snapshot: {snapshot} (signature={sig})")
        plan_lines.append(f"Data root: {Path(data_root).resolve()}")
        plan_lines.append(f"Steps dir: {steps_root}")
        plan_lines.append(f"DuckDB:    {duckdb_path or '(not provided)'}")
        plan_lines.append("Plan order:")
        if prelude:
            plan_lines.append(f"  00: {prelude.relative_to(steps_root)}")
        if macros:
            plan_lines.append(f"  01: {macros.relative_to(steps_root)}")
        for i, p in enumerate(steps, start=2):
            plan_lines.append(f"  {i:02d}: {p.relative_to(steps_root)}")
        log.info("\n" + "\n".join(plan_lines))
        return

    # ---- Execute plan ------------------------------------------------------
    strict = True  # stop on first failure for now
    sig = _snapshot_signature(snapshot)
    data_root_p = Path(data_root)
    snapshot_root = (data_root_p / "bronze" / "snapshots" / snapshot).resolve()
    run_dir = (data_root_p / "silver" / sig / source / "_run").resolve()
    run_dir.mkdir(parents=True, exist_ok=True)

    if duckdb_path is None:
        raise ValueError("duckdb_path is required for execution")

    duckdb_path_p = Path(duckdb_path)
    duckdb_path_p.parent.mkdir(parents=True, exist_ok=True)
    conn = duckdb.connect(str(duckdb_path_p))
    # Session settings (aligned with prior notebook cell conventions)
    try:
        conn.execute("SET temp_directory='/tmp/duckdb_tmp'")
        conn.execute("SET memory_limit='50GB'")
        conn.execute("SET threads=1")
        conn.execute("SET preserve_insertion_order=false")
    except Exception:
        # Non-fatal if some settings unsupported on older DuckDBs
        pass

    # Shared variables for templating and Python globals
    varmap: dict[str, str] = {
        "DATA_ROOT": str(data_root_p.resolve()),
        "SNAPSHOT": snapshot,
        "SIGNATURE": sig,
        "SNAPSHOT_ROOT": str(snapshot_root),
        "SILVER_DUCKDB_PATH": str(duckdb_path_p.resolve()),
    }

    executed_path = run_dir / "executed.jsonl"

    def _log_exec(rec: dict) -> None:
        with executed_path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")

    def _run_sql_file(path: Path) -> None:
        started = datetime.utcnow().isoformat() + "Z"
        t0 = time.time()
        text = path.read_text(encoding="utf-8")
        text = _strip_sql_magics(text)
        # simple templating first
        text = _subst_vars(text, varmap)
        # best-effort replacement of hardcoded bronze snapshot path
        legacy = f"data/bronze/snapshots/{snapshot}"
        text = text.replace(legacy, varmap["SNAPSHOT_ROOT"]) if legacy in text else text
        try:
            conn.execute("BEGIN")
            stmts = _split_sql_statements(text)
            if not stmts:
                conn.execute("COMMIT")
            else:
                for s in stmts:
                    conn.execute(s)
                conn.execute("COMMIT")
            dur = int((time.time() - t0) * 1000)
            _log_exec({
                "file": str(path), "type": "sql", "status": "ok",
                "started_at": started, "finished_at": datetime.utcnow().isoformat() + "Z",
                "duration_ms": dur, "statements": len(stmts),
            })
            log.info(f"Executed SQL: {path.name} ({len(stmts)} statements, {dur} ms)")
        except Exception as e:
            try:
                conn.execute("ROLLBACK")
            except Exception:
                pass
            dur = int((time.time() - t0) * 1000)
            _log_exec({
                "file": str(path), "type": "sql", "status": "error",
                "started_at": started, "finished_at": datetime.utcnow().isoformat() + "Z",
                "duration_ms": dur, "error": str(e),
            })
            log.exception(f"SQL step failed: {path}")
            if strict:
                raise

    def _run_py_file(path: Path) -> None:
        started = datetime.utcnow().isoformat() + "Z"
        t0 = time.time()
        code = path.read_text(encoding="utf-8")
        # templating for python too (allows ${SNAPSHOT_ROOT} usage)
        code = _subst_vars(code, varmap)
        # legacy replacement
        legacy = f"data/bronze/snapshots/{snapshot}"
        code = code.replace(legacy, varmap["SNAPSHOT_ROOT"]) if legacy in code else code

        gbls: dict[str, object] = {
            "conn": conn,
            "Path": Path,
            "json": json,
            "os": os,
            "glob": glob,
            "tempfile": __import__("tempfile"),
            "pd": pd,
            "pq": pq,
            "duckdb": duckdb,
            # variables
            "DATA_ROOT": varmap["DATA_ROOT"],
            "SNAPSHOT": varmap["SNAPSHOT"],
            "SIGNATURE": varmap["SIGNATURE"],
            "SNAPSHOT_ROOT": varmap["SNAPSHOT_ROOT"],
            "SILVER_DUCKDB_PATH": varmap["SILVER_DUCKDB_PATH"],
        }
        try:
            compiled = compile(code, filename=str(path), mode="exec")
            exec(compiled, gbls)
            dur = int((time.time() - t0) * 1000)
            _log_exec({
                "file": str(path), "type": "py", "status": "ok",
                "started_at": started, "finished_at": datetime.utcnow().isoformat() + "Z",
                "duration_ms": dur,
            })
            log.info(f"Executed PY: {path.name} ({dur} ms)")
        except Exception as e:
            dur = int((time.time() - t0) * 1000)
            _log_exec({
                "file": str(path), "type": "py", "status": "error",
                "started_at": started, "finished_at": datetime.utcnow().isoformat() + "Z",
                "duration_ms": dur, "error": str(e),
            })
            log.exception(f"Python step failed: {path}")
            if strict:
                raise

    # Execute in sequence: prelude, macros, steps
    order: list[tuple[str, Path]] = []
    if prelude:
        order.append(("py", prelude))
    if macros:
        order.append(("sql", macros))
    for p in steps:
        order.append((p.suffix.lstrip("."), p))

    for kind, path in order:
        if kind == "sql":
            _run_sql_file(path)
        elif kind == "py":
            _run_py_file(path)
        else:
            log.warning(f"Skipping unsupported file type: {path}")
    return


async def silver_camara(
    snapshot: str,
    data_root: str = "./data",
    duckdb_path: str | os.PathLike[str] | None = None,
    steps_dir: str | os.PathLike[str] | None = None,
    dry_run: bool = False,
) -> None:
    """Async Câmara silver pipeline facade."""
    await _run_silver_source(
        source="camara",
        snapshot=snapshot,
        data_root=data_root,
        duckdb_path=duckdb_path,
        steps_dir=steps_dir,
        dry_run=dry_run,
    )


async def silver_senado(
    snapshot: str,
    data_root: str = "./data",
    duckdb_path: str | os.PathLike[str] | None = None,
    steps_dir: str | os.PathLike[str] | None = None,
    dry_run: bool = False,
) -> None:
    """Async Senado silver pipeline facade."""
    await _run_silver_source(
        source="senado",
        snapshot=snapshot,
        data_root=data_root,
        duckdb_path=duckdb_path,
        steps_dir=steps_dir,
        dry_run=dry_run,
    )


def run_silver(
    source: str,
    snapshot: str,
    data_root: str = "./data",
    duckdb_path: str | os.PathLike[str] | None = None,
    steps_dir: str | os.PathLike[str] | None = None,
    dry_run: bool = False,
) -> None:
    """Run the Silver pipeline for a given source via asyncio."""
    if source == "camara":
        asyncio.run(
            silver_camara(
                snapshot=snapshot,
                data_root=data_root,
                duckdb_path=duckdb_path,
                steps_dir=steps_dir,
                dry_run=dry_run,
            )
        )
    elif source == "senado":
        asyncio.run(
            silver_senado(
                snapshot=snapshot,
                data_root=data_root,
                duckdb_path=duckdb_path,
                steps_dir=steps_dir,
                dry_run=dry_run,
            )
        )
    elif source == "all":
        # Run both sequentially
        asyncio.run(
            silver_camara(
                snapshot=snapshot,
                data_root=data_root,
                duckdb_path=duckdb_path,
                steps_dir=steps_dir,
                dry_run=dry_run,
            )
        )
        asyncio.run(
            silver_senado(
                snapshot=snapshot,
                data_root=data_root,
                duckdb_path=duckdb_path,
                steps_dir=steps_dir,
                dry_run=dry_run,
            )
        )
    else:
        raise ValueError("source must be one of: camara, senado, all")
