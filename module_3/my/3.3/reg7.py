import re

x = re.match(r"text", "TEXT", re.IGNORECASE)
print(x)

x = re.match(r"(te)*?xt", "TEXTTEXT", re.IGNORECASE | re.DEBUG)
print(x)