import sys
import re

for line in sys.stdin:
    line = line.rstrip()

    pattern = r"z...z"
    all_inclusions = re.findall(pattern, line)
    #print(all_inclusions)
    if len(all_inclusions) >= 1:
        print(line)
