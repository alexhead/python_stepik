import re
import sys
import requests

def func_del_pair(l):
    n = []
    for i in l:
        if i not in n:
            n.append(i)
    return n

res = requests.get(str(input()))
spis = []

with open("python.html", "wb") as f:
    f.write(res.content)

f = open("python.html")
for line in f:
    line = line.rstrip()
    pattern = r'<a\s.*\bhref=[\'\"][aA-zZ]'
    all_inclusions = re.findall(pattern, line)

    if len(all_inclusions) >= 1:
        #print(line)
        pattern = r'.*a.*href=[\"\']'
        repl = ""
        line = re.sub(pattern, repl, line, count=0)

        pattern = r'http[s]?[\:][\/][\/]'
        repl = ""
        line = re.sub(pattern, repl, line, count=0)

        pattern = r'[f][t][p][\:][\/][\/]'
        repl = ""
        line = re.sub(pattern, repl, line, count=0)
        #print(line)
        pattern = r'[/\:\"\'].*'
        repl = ""
        line = re.sub(pattern, repl, line, count=0)
        spis.append(line)
       # print(line)

f.close()
a = func_del_pair(spis)
a = sorted(a)

for i in range(len(a)):
   print(a[i])




