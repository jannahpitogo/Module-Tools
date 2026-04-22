from pathlib import Path

path = "sample-files/3.txt"

content = Path(path).read_text(encoding="utf-8")
lines = len(content.split("\n"))

print(lines, path)