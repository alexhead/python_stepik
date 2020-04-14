import re

pattern = r"((abc)|(test|text)*)"
string = "texttest"

match = re.match(pattern, string)
print(match)
print(match.groups())

pattern = r"Hello (abc|test)"
string = "Hello abc"
match = re.match(pattern, string)
print(match)
print(match.group(0))
print(match.group(1))