import re
import sys
import requests


res = requests.get(str(input()))

# print(res.status_code)
# print(res.headers['Content-Type'])

# print(res.content)
# print(res.text)

with open("python.html", "wb") as f:
    f.write(res.content)

f = open("python.html")
for line in f:
    line = line.rstrip()
    pattern = r"a\s\bhref=\w*"


    all_inclusions = re.findall(pattern, line)


    if len(all_inclusions) >= 1:

        pattern = r"[=]\w*"
        #pattern = r"=\w*"
        in_cut = re.findall(pattern, line)
        if len(in_cut) >= 1:
            print(line)

f.close()


