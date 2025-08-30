from pathlib import Path

SRC_DIR = Path("./src/tramita")


def tag_file(file_path: Path, tag_text: str):
    lines: list[str] = file_path.read_text().splitlines()
    while lines and (lines[0].strip() == "" or lines[0].startswith("#")):
        lines.pop(0)

    header_lines = [
        f"# {tag_text}",
        ""
    ]

    lines = header_lines + lines
    tagged_text = "\n".join(lines)
    file_path.write_text(tagged_text)


for filename in SRC_DIR.rglob("*.py"):
    rel_path = filename.relative_to(SRC_DIR)
    tag_file(filename, str(rel_path))
