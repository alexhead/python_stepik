s = str(input())
t = str(input())
k = 0
w = []
for i in range(len(s)):
    z = s.find(t, i)
    if z >= 0:
        w.append(z)

w = list(set(w))
print(len(w))
