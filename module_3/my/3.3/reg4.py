import re

pattern = r"ab*a"
string = "aa, aba, abba"

all_inclusions = re.findall(pattern, string)
print(all_inclusions)

