import sys
import re



for line in sys.stdin:
    line = line.rstrip()
    #print(line)
    pattern = "cat"
    all_inclusions = re.findall(pattern, line)

    if len(all_inclusions) >= 2:
        print(line)


