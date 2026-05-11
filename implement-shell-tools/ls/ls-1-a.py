from pathlib import Path

pathDir = Path("sample-files")

try:
    print(".\n..")
    for file in pathDir.iterdir():
        print(file.name)
except Exception as err:
    print(err)