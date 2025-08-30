# tests/test_parquet.py

from pathlib import Path
import pyarrow.parquet as pq

from tramita.storage.paths import BronzePaths
from tramita.storage.manifest import new_manifest
from tramita.storage.parquet import write_details_parts, write_index_parquet


def test_write_index_and_details(tmp_path: Path):
    paths = BronzePaths(data_root=tmp_path, snapshot="bronze-2020-2024-v1")
    paths.ensure_base_dirs()
    paths.set_latest_symlink()
    manifest = new_manifest(snapshot_name=paths.root.name)

    # index
    idx_path = paths.index_file("camara", "proposicoes", 2020)
    n_idx = write_index_parquet([
        {"source": "camara", "entity": "proposicoes",
            "year": 2020, "id": "1", "url": "u1"},
        {"source": "camara", "entity": "proposicoes",
            "year": 2020, "id": "2", "url": "u2"},
    ], idx_path)
    assert n_idx == 2
    assert idx_path.exists()

    # details (two rows -> single part)
    rows = [
        {"source": "camara", "entity": "proposicoes", "year": 2020,
            "id": "2", "url": "u2", "payload_json": {"a": 2}},
        {"source": "camara", "entity": "proposicoes", "year": 2020,
            "id": "1", "url": "u1", "payload_json": {"a": 1}},
    ]
    parts = write_details_parts(
        rows,
        paths=paths,
        manifest=manifest,
        source="camara",
        entity="proposicoes",
        year=2020,
        part_rows=50_000,
        sort=True,
    )
    assert len(parts) == 1
    table = pq.read_table(parts[0])
    assert table.num_rows == 2
    # ensure sorted by id asc (1,2)
    ids = table.column("id").to_pylist()
    assert ids == ["1", "2"]
