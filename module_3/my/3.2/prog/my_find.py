s = str(input())
a = str(input())
b = str(input())

k = 0
e = 0

while (s.count(a) > 0):
    if b.count(a) == 0:
        s = s.replace(a, b)
        k += 1
    else:
        print("Impossible")
        e += 1
        break

if e == 0:
    print(k)
