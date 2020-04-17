import re

# print(re.match)
# print(re.search)
# print(re.findall)
# print(re.sub)



pattern = r"a[a-zA-Z]c"
string = "aacd, acc, aac, azc"
match_object = re.match(pattern, string)
print(match_object)

string = "abxcsac, acc, aac, azc"
all_inclusions = re.findall(pattern, string)
print(all_inclusions)

fixed_typos = re.sub(pattern, "abc", string)
print(fixed_typos)