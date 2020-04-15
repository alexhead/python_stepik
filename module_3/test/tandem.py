import sys
import re

for line in sys.stdin:
    line = line.rstrip()

    pattern = r"\b((\w+?)\2)\b"
    all_inclusions = re.findall(pattern, line)

    if len(all_inclusions) >= 1:
        print(line)
