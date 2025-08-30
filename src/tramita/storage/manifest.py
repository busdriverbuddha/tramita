# tramita/storage/manifest.py

import hashlib
import platform
import subprocess
import sys

from pathlib import Path

from pydantic import BaseModel, Field


def sha256_file(path: Path, bufsize: int = 1024 * 1024) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        while True:
            b = f.read(bufsize)
            if not b:
                break
            h.update(b)
    return h.hexdigest()


class FileEntry(BaseModel):
    path: str         # path relative to snapshot root
    rows: int
    bytes: int
    sha256: str


class YearSummary(BaseModel):
    total_rows: int = 0
    total_bytes: int = 0
    files: list[FileEntry] = Field(default_factory=list)
    agg_sha256: str | None = None  # sha256 of concatenated file hashes (sorted by path)

    def finalize(self):
        # deterministic: sort by path name
        self.files.sort(key=lambda f: f.path)
        cat = "".join(f.sha256 for f in self.files).encode()
        self.agg_sha256 = hashlib.sha256(cat).hexdigest()


class EntitySummary(BaseModel):
    years: dict[str, YearSummary] = Field(default_factory=dict)  # "2020": YearSummary


class SourceSummary(BaseModel):
    entities: dict[str, EntitySummary] = Field(default_factory=dict)  # "proposicoes": EntitySummary, etc.


class SnapshotManifest(BaseModel):
    snapshot_name: str
    created_at: str            # ISO8601
    python: str
    platform: str
    git_commit: str | None = None
    app_version: str | None = None
    sources: dict[str, SourceSummary] = Field(default_factory=dict)  # "camara": SourceSummary

    def add_file(
        self,
        snapshot_root: Path,
        source: str,
        entity: str,
        year: int,
        file_path: Path,
        rows: int
    ) -> None:
        rel = file_path.relative_to(snapshot_root).as_posix()
        size = file_path.stat().st_size
        file_hash = sha256_file(file_path)
        src = self.sources.setdefault(source, SourceSummary())
        ent = src.entities.setdefault(entity, EntitySummary())
        ys = ent.years.setdefault(str(year), YearSummary())
        ys.files.append(FileEntry(path=rel, rows=rows, bytes=size, sha256=file_hash))
        ys.total_rows += rows
        ys.total_bytes += size

    def finalize(self) -> None:
        for src in self.sources.values():
            for ent in src.entities.values():
                for ys in ent.years.values():
                    ys.finalize()

    def save(self, path: Path) -> None:
        self.finalize()
        path.parent.mkdir(parents=True, exist_ok=True)
        text = self.model_dump_json(indent=2)
        path.write_text(text, encoding="utf-8")


def iso_now() -> str:
    from datetime import datetime, timezone
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def get_git_commit() -> str | None:
    try:
        return (
            subprocess.check_output(["git", "rev-parse", "HEAD"], stderr=subprocess.DEVNULL)
            .decode().strip()
        )
    except Exception:
        return None


def new_manifest(snapshot_name: str, app_version: str | None = None) -> SnapshotManifest:
    return SnapshotManifest(
        snapshot_name=snapshot_name,
        created_at=iso_now(),
        python=sys.version.split()[0],
        platform=f"{platform.system()} {platform.release()}",
        git_commit=get_git_commit(),
        app_version=app_version,
    )


def verify_against_manifest(snapshot_root: Path, manifest: SnapshotManifest) -> list[str]:
    """
    Recompute SHA and size on disk; return a list of human-readable problems.
    """
    problems: list[str] = []
    for source, src in manifest.sources.items():
        for entity, ent in src.entities.items():
            for year, ys in ent.years.items():
                # recompute file hashes and sizes
                for fe in ys.files:
                    p = snapshot_root / fe.path
                    if not p.exists():
                        problems.append(f"Missing file: {fe.path}")
                        continue
                    bytes_now = p.stat().st_size
                    hash_now = sha256_file(p)
                    if bytes_now != fe.bytes:
                        problems.append(f"Size mismatch: {fe.path} expected {fe.bytes}, got {bytes_now}")
                    if hash_now != fe.sha256:
                        problems.append(f"SHA mismatch: {fe.path} expected {fe.sha256}, got {hash_now}")
                # recompute agg sha
                files_sorted = sorted(ys.files, key=lambda f: f.path)
                cat = "".join(f.sha256 for f in files_sorted).encode()
                agg_now = hashlib.sha256(cat).hexdigest()
                if ys.agg_sha256 and agg_now != ys.agg_sha256:
                    problems.append(f"Aggregate SHA mismatch for {source}/{entity}/{year}")
    return problems