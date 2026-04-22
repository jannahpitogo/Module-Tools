from pathlib import Path

dir_path = Path(__file__).parent / "sample-files"
files = list(dir_path.iterdir())

total_lines = 0
total_words = 0
total_bytes = 0

file_count = 0

for file in files:
    if not file.is_file():
        continue

    content = file.read_text(encoding="utf-8")
    lines = len(content.split("\n"))
    words = len(content.strip().split()) if content.strip() else 0
    byte_count = len(content.encode("utf-8"))

    total_lines += lines
    total_words += words
    total_bytes += byte_count
    file_count += 1

    print(lines, words, byte_count, file.name)

if file_count > 1:
    print(total_lines, total_words, total_bytes, "total")