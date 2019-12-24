a = int(input())

objects = []

for i in range(a):
	objects.append(input())

s = []
for obj in objects:
    if obj not in s:
        s.append(obj)
print(len(s))