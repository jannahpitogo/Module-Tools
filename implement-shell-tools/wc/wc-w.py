from pathlib import Path

path = "sample-files/3.txt"

content = Path(path).read_text(encoding="utf-8")
words = len(content.strip().split()) if content.strip() else 0

print(words, path)