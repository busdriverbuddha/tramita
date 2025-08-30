from pathlib import Path

SRC_DIR = Path("./src/tramita")

for filename in SRC_DIR.rglob("*.py"):
    print(filename.relative_to(SRC_DIR))
