
f = open("test_1.txt", "w")
f.write("Hello")
f.write("World\n")

lines = ["Line1", "Line2", "Line3"]
contents = "\n".join(lines)
f.write(contents)
f.close()
