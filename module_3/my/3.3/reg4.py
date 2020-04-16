import re

pattern = r"ab*a"
string = "aa, aba, abba, ashbxha"

all_inclusions = re.findall(pattern, string)
print(all_inclusions)

