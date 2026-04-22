from pathlib import Path

pathFile = Path("sample-files")

data = sorted(f for f in pathFile.iterdir() if f.suffix == ".txt")

line_number = 1

for item in data:
    lines = item.read_text(encoding="utf-8").split("\n")

    for line in lines:
        if len(line) > 0:
            print(f"{line_number} {line}")
            line_number += 1