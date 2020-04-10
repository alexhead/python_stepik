import re

# print(re.match)
# print(re.search)
# print(re.findall)
# print(re.sub)

pattern = r"abc"
string = "abcd"
match_object = re.match(pattern, string)
print(match_object)

pattern = r"a[abc]c"
string = "aacd"
match_object = re.match(pattern, string)
print(match_object)

string = "abc, acc, aac"
all_inclusions = re.findall(pattern, string)
print(all_inclusions)

fixed_typos = re.sub(pattern, "abc", string)
print(fixed_typos)