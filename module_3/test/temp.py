import re

string = 'baTAAreTheBestaaaaabbbbaaaaaaa'

#1 replace chars that occur more then twice
tmp = ''
while tmp != string:
  tmp = string
  string = re.sub(r'(\w)(((.*)\1){2,})', r')\2', tmp)
  print(string)
