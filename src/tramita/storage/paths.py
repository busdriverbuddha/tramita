# src/tramita/storage/paths.py

import os

from dataclasses import dataclass
from pathlib import Path

PART_FMT = "part-{idx:05d}.parquet"


@dataclass(frozen=True)
class BronzePaths:
    data_root: Path
    snapshot: str

    @property
    def root(self) -> Path:
        return self.data_root / "bronze" / "snapshots" / self.snapshot

    @property
    def latest_symlink(self) -> Path:
        return self.data_root / "bronze" / "snapshots" / "latest"

    def source_root(self, source: str) -> Path:
        # source: "camara" | "senado"
        return self.root / source

    def entity_stage_dir(self, source: str, entity: str, stage: str) -> Path:
        # stage: "index" | "details" | "tramitacoes" | "autores" | "votacoes" (etc.)
        return self.source_root(source) / entity / stage

    def index_file(self, source: str, entity: str, year: int) -> Path:
        # single file holding IDs/URIs for that year
        return self.entity_stage_dir(source, entity, "index") / f"year={year}" / "ids.parquet"

    def details_part_dir(self, source: str, entity: str, year: int) -> Path:
        return self.entity_stage_dir(source, entity, "details") / f"year={year}"

    def details_part_file(self, source: str, entity: str, year: int, part_idx: int) -> Path:
        return self.details_part_dir(source, entity, year) / PART_FMT.format(idx=part_idx)

    def relation_part_dir(self, source: str, relation: str, year: int) -> Path:
        # e.g., relation in {"tramitacoes","autores","votacoes"}; grouped by relation
        return self.source_root(source) / relation / f"year={year}"

    def relation_part_file(self, source: str, relation: str, year: int, part_idx: int) -> Path:
        return self.relation_part_dir(source, relation, year) / PART_FMT.format(idx=part_idx)

    @property
    def logs_dir(self) -> Path:
        return self.root / "_logs"

    @property
    def failed_ids_csv(self) -> Path:
        return self.logs_dir / "failed_ids.csv"

    @property
    def manifest_json(self) -> Path:
        return self.root / "manifest.json"

    def ensure_base_dirs(self) -> None:
        for p in [self.root, self.logs_dir]:
            p.mkdir(parents=True, exist_ok=True)

    def set_latest_symlink(self) -> None:
        self.ensure_base_dirs()
        latest = self.latest_symlink
        try:
            if latest.is_symlink() or latest.exists():
                latest.unlink()
        except FileNotFoundError:
            pass
        # Create relative symlink for portability
        target = Path(os.path.relpath(self.root, latest.parent))
        latest.symlink_to(target, target_is_directory=True)
