import sys
import re

for line in sys.stdin:
    line = line.rstrip()

    pattern = r"\b\w*\b"
    fixed_typos = re.findall(pattern, line)
    a = int(len(fixed_typos)/2)
    print(a)
    i = 0
    t= ''

    for i in range(a):
        text = fixed_typos[1]

        print(text)
        n = text[0]
        s = text[1]
        text = text[1] + text[0] + text[2:]
        #text += ' '
        i += 1
        t += text
    print(t)





