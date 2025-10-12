# tramita/cli.py

import typer

from tramita.pipelines.bronze import run_bronze, verify_bronze

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


if __name__ == "__main__":
    app()
