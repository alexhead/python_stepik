x = [
    ("Guido", "Van", "Rossum"),
    ("Haskell", "Curry"),
    ("John", "Backus")
]

#def length(name):
 #   return len(" ".join(name))

#name_lengths = [length(name) for name in x]
#print(name_lengths)
# идентичная запись
x.sort(key=lambda name: len(" ".join(name)))
print(x)

import operator as op
x.sort(key=op.itemgetter(0))
print(x)

