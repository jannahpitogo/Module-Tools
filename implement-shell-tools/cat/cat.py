from pathlib import Path
import sys

try: 
    data = sys.argv[1]
    content = Path(data).read_text(encoding="utf-8")
    sys.stdout.write(content)
except:
    sys.stderr.write(f"cat: {data}: No file available")