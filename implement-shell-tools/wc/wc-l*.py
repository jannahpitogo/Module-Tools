from pathlib import Path

folder = "sample-files"
dir_path = Path(__file__).parent / folder

total = 0

for file in dir_path.iterdir():
    if not file.is_file():
        continue

    content = file.read_text(encoding="utf-8")
    lines = len(content.split("\n"))
    total += lines

    print(lines, file.name)

print(total, "total")