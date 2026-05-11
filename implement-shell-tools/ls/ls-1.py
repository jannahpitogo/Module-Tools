from pathlib import Path

current_dir = Path(__file__).parent

try:
    for file in current_dir.iterdir():
        print(file.name)
except Exception as err:
    print(err)