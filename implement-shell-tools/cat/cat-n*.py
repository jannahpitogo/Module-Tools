from pathlib import Path

pathFile = Path("sample-files")

files = sorted(f for f in pathFile.iterdir() if f.suffix == ".txt")

line_number = 1

for file in files:
    lines = file.read_text(encoding="utf-8").split("\n")

    for line in lines:
        print(f"{line_number}\t{line}")
        line_number += 1