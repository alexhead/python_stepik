import operator as op

print(op.add(4, 5))
print(op.mul(4, 5))
print(op.contains([1, 2, 3], 4)) # 4 in [1, 2, 3]

x = [1, 2, 3]
f = op.itemgetter(1) # f(x) == x[1}
print(f(x))