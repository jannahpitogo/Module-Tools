from pathlib import Path

path = "sample-files/3.txt"

content = Path(path).read_bytes()  # read raw bytes
print(len(content), path)