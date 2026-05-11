import sys
from pathlib import Path

try:
    filePath = Path("sample-files/1.txt")
    content = filePath.read_text(encoding="utf-8").split("\n")
    for index, item in enumerate(content):
        print(f"{index + 1} {item}")
except FileNotFoundError: 
    sys.stderr.write(f"cat: {filePath}: Wrong path, No File Error")

