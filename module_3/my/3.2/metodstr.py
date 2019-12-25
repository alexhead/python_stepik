#print("abc" in "abcba")
#print("abce" in "abcba")

#print("cabcd".find("abc"))
#print(str.find.__doc__)

# print("cabcd".index("abc"))
# print("cabcd".index("aec"))

#s = "The woman in black fked across the desert..."
#print(s.startswith(("The woman", "The dog", "The man in black")))
# print(s.startswith.__doc__)

#s = "image.png"
#print(s.endswith(".png"))

#s = "abacaba"
#print(s.count("aba"))
#print(s.count.__doc__)
#print(s.find("aba"))
#print(s.rfind("aba")) # искать справа

#s = "The man in black fied across the desert, and the gunslinger followed"
#print(s.lower())
#print(s.upper())
#print(s.count("the"))
#print(s.lower().count("the"))

#s = "1,2,3,4"
#print(s)
#print(s.replace(",", ", "))
#print(s.replace.__doc__)

#s = "1 2 3 4"
#print(s.split(" "))
#print(s.split.__doc__)

#s = "      1, 2, 3, 4,     "
#print(repr(s.rstrip()))
#print(repr(s.lstrip()))
#print(repr(s.strip()))

numbers = map(str, [1, 2, 3, 4, 5])
print(repr(" x".join(numbers)))