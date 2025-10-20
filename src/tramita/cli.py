# tramita/cli.py

import os
from pathlib import Path
import typer

from tramita.pipelines.bronze import run_bronze, verify_bronze
from tramita.pipelines.silver import run_silver

def _load_env_from_dotenv() -> None:
    """Load environment variables from a .env file if present.

    Tries python-dotenv first; if unavailable, falls back to a simple parser for
    KEY=VALUE lines (ignores comments and blank lines). Existing environment
    variables are not overwritten by the fallback.
    """
    # Try python-dotenv if installed
    try:
        from dotenv import load_dotenv  # type: ignore

        load_dotenv()  # loads from .env in CWD if present
        return
    except Exception:
        pass

    # Minimal fallback: parse .env in current working directory
    env_path = Path(".env")
    if not env_path.exists():
        return
    try:
        for raw in env_path.read_text(encoding="utf-8").splitlines():
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            if "=" not in line:
                continue
            key, val = line.split("=", 1)
            key = key.strip()
            val = val.strip().strip('"').strip("'")
            os.environ.setdefault(key, val)
    except Exception:
        # Silently ignore malformed .env; users can fix or install python-dotenv
        pass


_load_env_from_dotenv()


app = typer.Typer(no_args_is_help=True)


@app.command()
def bronze(
    source: str = typer.Argument("all", help="camara|senado|all"),
    years: str = typer.Option("2020-2024", help="e.g. 2020-2024 or 2020,2021"),
    snapshot: str = typer.Option("bronze-2020-2024-v2"),
    data_root: str = typer.Option("./data"),
    types: str = typer.Option("", help="Comma-separated siglaTipo filter, e.g. 'PL,PEC'"),
    sample: str = typer.Option("", help="Deterministic downsample like '1/200' (~0.5%)"),
    window_days: int = typer.Option(30, help="Window size in days for tramitação scan"),
    page_size: int = typer.Option(100, help="Items per page for API calls"),
    start: str = typer.Option("", help="Optional start date YYYY-MM-DD (overrides years start)"),
    end: str = typer.Option("", help="Optional end date YYYY-MM-DD (overrides years end)"),
    autores: bool = typer.Option(True, "--autores/--no-autores", help="Fetch autores relations + author entities"),
    resume_from: str = typer.Option("all", help="Resume from stage (e.g. 'tramitacoes')"),
):
    """Run Bronze ingestion."""
    run_bronze(
        source, years, snapshot, data_root,
        types=types, sample=sample,
        window_days=window_days, page_size=page_size,
        start=start, end=end,
        autores=autores,
        resume_from=resume_from,
    )


@app.command()
def verify(
    target: str = typer.Argument("bronze"),
    snapshot: str = typer.Option("bronze-2020-2024-v2"),
    data_root: str = typer.Option("./data"),
):
    """Verify Bronze manifest and files."""
    if target != "bronze":
        raise typer.BadParameter("Only 'bronze' is supported for now.")
    code = verify_bronze(snapshot, data_root)
    raise typer.Exit(code)


@app.command()
def silver(
    source: str = typer.Argument("camara", help="camara|senado|all"),
    snapshot: str = typer.Option("bronze-2020-2024-v2", help="Bronze snapshot name to read from"),
    data_root: str = typer.Option("./data", help="Data root directory"),
    duckdb_path: str = typer.Option(
        default_factory=lambda: __import__("os").environ.get("SILVER_DUCKDB_PATH", ""),
        help="Path to the Silver DuckDB file (must include snapshot signature)",
    ),
    steps_dir: str = typer.Option(
        "",
        help="Directory under data_root containing step files (.sql/.py); if empty, defaults based on snapshot signature",
    ),
    dry_run: bool = typer.Option(False, help="List planned steps and exit without executing"),
):
    """Run Silver pipeline (Câmara) using user-supplied steps under data_root."""
    if not duckdb_path:
        raise typer.BadParameter(
            "duckdb_path is required (set --duckdb-path or SILVER_DUCKDB_PATH)"
        )

    run_silver(
        source=source,
        snapshot=snapshot,
        data_root=data_root,
        duckdb_path=duckdb_path,
        steps_dir=steps_dir or None,
        dry_run=dry_run,
    )


if __name__ == "__main__":
    app()
