import sys
import re

for line in sys.stdin:
    line = line.rstrip()

    pattern = r"\b[aA-zZ]*[aA-zZ]\b"
    fixed_typos = re.sub(pattern, "argh", line, count=1)
    print(fixed_typos)