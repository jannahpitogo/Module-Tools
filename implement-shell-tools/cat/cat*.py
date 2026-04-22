from pathlib import Path
import sys

try: 
    data = sys.argv[3:]

    for item in data:
        content = Path(item).read_text(encoding="utf-8")
        print(content, end="")
except FileNotFoundError:
        sys.stderr.write(f"cat: {item}: No such file or directory\n")