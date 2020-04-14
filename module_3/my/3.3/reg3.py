import re
# [] -- можно указать множ-во подход. символов
# , ^ $ * + ? { } [ ] \ | ( ) -- метасимволы
# \d - [0-9] -- цифры
# \D - [^0-9]
# \s - [ \t\n\r\f\v] -- пробельные символы
# \S - [^ \t\n\r\f\v] -- пробельные символы
# \w - [a-zA-Z0-9_] -- буквы + цифры + _
# \W - [^a-zA-Z0-9_] -- буквы + цифры + _

pattern = r" english\?"
string = "Do you speak english?"
match = re.search(pattern, string)
print(match)