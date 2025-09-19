# tramita/ui.py

import sys
from contextlib import contextmanager
from typing import Callable, Iterator

from rich.console import Console
from rich.progress import (
    Progress, SpinnerColumn, TextColumn, BarColumn,
    TaskProgressColumn, MofNCompleteColumn, TimeElapsedColumn,
    TimeRemainingColumn, ProgressColumn
)
from rich.text import Text


class RemainingCallsColumn(ProgressColumn):
    """Display remaining items as a small counter."""
    def render(self, task) -> Text:  # type: ignore[override]
        remaining = int((task.total or 0) - task.completed)
        return Text(f"left {remaining}")


def _stderr_console() -> Console:
    # Keep progress separate from logs (your logs go to stdout)
    return Console(file=sys.stderr, force_terminal=sys.stderr.isatty())


@contextmanager
def progress_reporter(total: int, description: str = "requests") -> Iterator[Callable[[int, int], None]]:
    # Only show in interactive terminals; otherwise become a no-op.
    if total <= 1 or not sys.stderr.isatty():
        yield lambda done, tot: None
        return

    console = _stderr_console()
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TaskProgressColumn(),            # e.g., 37%
        MofNCompleteColumn(),            # e.g., 123/500
        RemainingCallsColumn(),          # e.g., left 377
        TimeElapsedColumn(),
        TimeRemainingColumn(),
        transient=True,                  # erase bar when done
        console=console,
        refresh_per_second=10,
    ) as p:
        task = p.add_task(description, total=total)

        def on_progress(done: int, tot: int) -> None:
            # Update completed count; columns compute the rest
            p.update(task, completed=done)

        yield on_progress
