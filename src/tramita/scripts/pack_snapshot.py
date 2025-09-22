# tramita/scripts/pack_snapshot.py

import argparse
import hashlib
import tarfile

from pathlib import Path


try:
    import zstandard as zstd
    HAVE_ZSTD = True
except ImportError:
    HAVE_ZSTD = False

CHUNK = 1024 * 1024


def human_to_bytes(s: str) -> int:
    s = s.strip().upper()
    units = {"B": 1, "KB": 1024, "MB": 1024**2, "GB": 1024**3}
    for u in ("GB", "MB", "KB", "B"):
        if s.endswith(u):
            return int(float(s[:-len(u)]) * units[u])
    # default MB if bare number
    return int(float(s) * 1024**2)


def sha256_file(path: Path, bufsize: int = CHUNK) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        while True:
            b = f.read(bufsize)
            if not b:
                break
            h.update(b)
    return h.hexdigest()


def make_tar_zst(src_dir: Path, out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    if HAVE_ZSTD:
        cctx = zstd.ZstdCompressor(level=10)  # type: ignore
        with out_path.open("wb") as out_fh, cctx.stream_writer(out_fh) as compressor:
            with tarfile.open(mode="w|", fileobj=compressor) as tar:
                tar.add(src_dir, arcname=src_dir.name, recursive=True)
    else:
        # Fallback to gz if zstandard not installed
        with tarfile.open(out_path.with_suffix(".tar.gz"), mode="w:gz") as tar:
            tar.add(src_dir, arcname=src_dir.name, recursive=True)


def make_tar(src_dir: Path, out_base: Path) -> Path:
    """
    Create tarball; prefer .tar.zst if zstd available, else .tar.gz.
    Returns the actual output path created.
    """
    out_base.parent.mkdir(parents=True, exist_ok=True)
    if HAVE_ZSTD:
        out_path = out_base  # e.g., foo.tar.zst
        cctx = zstd.ZstdCompressor(level=10)  # type: ignore
        with out_path.open("wb") as out_fh, cctx.stream_writer(out_fh) as compressor:
            with tarfile.open(mode="w|", fileobj=compressor) as tar:
                tar.add(src_dir, arcname=src_dir.name, recursive=True)
    else:
        out_path = out_base.with_suffix(".tar.gz")
        with tarfile.open(out_path, mode="w:gz") as tar:
            tar.add(src_dir, arcname=src_dir.name, recursive=True)
    return out_path


def split_file(path: Path, max_bytes: int) -> list[Path]:
    parts = []
    with path.open("rb") as src:
        idx = 1
        while True:
            chunk = src.read(max_bytes)
            if not chunk:
                break
            part = path.with_suffix(path.suffix + f".part{idx:02d}")
            with part.open("wb") as out:
                out.write(chunk)
            # write a sidecar .sha256 for each part
            (part.with_suffix(part.suffix + ".sha256")).write_text(sha256_file(part))
            parts.append(part)
            idx += 1
    return parts


def main():
    ap = argparse.ArgumentParser(description="Pack and split a Bronze snapshot for release.")
    ap.add_argument("--data-root", default="./data")
    ap.add_argument("--snapshot", required=True)
    ap.add_argument("--out", default="./artifacts")
    ap.add_argument("--max-part", default="1900MB")
    args = ap.parse_args()

    data_root = Path(args.data_root)
    snap_dir = data_root / "bronze" / "snapshots" / args.snapshot
    if not snap_dir.exists():
        raise SystemExit(f"Snapshot not found: {snap_dir}")

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    desired = out_dir / f"{args.snapshot}.tar.zst"
    print(f"[pack] Creating {desired} ...")
    tar_path = make_tar(snap_dir, desired)

    max_bytes = human_to_bytes(args.max_part)
    if tar_path.stat().st_size > max_bytes:
        print(f"[split] Splitting into ~{args.max_part} parts ...")
        parts = split_file(tar_path, max_bytes)
        manifest_txt = out_dir / f"{args.snapshot}.parts.txt"
        lines = [p.name + "\t" + sha256_file(p) for p in parts]
        manifest_txt.write_text("\n".join(lines) + "\n")
        print(f"[done] Wrote {len(parts)} parts + per-part .sha256 files.")
    else:
        (tar_path.with_suffix(tar_path.suffix + ".sha256")).write_text(sha256_file(tar_path))
        print("[done] Single file fits under max-part; wrote .sha256.")


if __name__ == "__main__":
    main()
