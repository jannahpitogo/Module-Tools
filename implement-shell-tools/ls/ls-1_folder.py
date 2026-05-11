from pathlib import Path

pathDir = Path("sample-files")

try:
    for file in pathDir.iterdir():
        print(file.name)
except Exception as err:
    print(err)