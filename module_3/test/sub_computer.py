import sys
import re

for line in sys.stdin:
    line = line.rstrip()

    pattern = r"human"
    fixed_typos = re.sub(pattern, "computer", line)
    print(fixed_typos)

