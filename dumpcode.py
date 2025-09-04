from pathlib import Path


def tag_file(file_path: Path, tag_text: str):
    lines: list[str] = file_path.read_text().splitlines()
    while lines and (lines[0].strip() == "" or lines[0].startswith("#")):
        lines.pop(0)

    header_lines = [
        f"# {tag_text}",
        ""
    ]

    lines = header_lines + lines
    tagged_text = "\n".join(lines) + "\n"
    file_path.write_text(tagged_text)


def main():
    SRC_DIR = Path("./src")
    dumps = []

    for filename in SRC_DIR.rglob("*.py"):
        old_text = filename.read_text()
        rel_path = filename.relative_to(SRC_DIR)
        tag_file(filename, str(rel_path))
        new_text = filename.read_text()
        if old_text != new_text:
            print(f"Tagged {rel_path}.")
        dumps.append(filename.read_text())

    divider = "\n# ------------------------------------------ #\n"

    dumptext = divider.join(dumps)

    with open("code-dump.txt", "w") as f:
        f.write(dumptext)

    print("Code dumped to code-dump.txt.")


if __name__ == "__main__":
    main()
