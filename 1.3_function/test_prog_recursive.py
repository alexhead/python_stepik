def recurs_f(a, b):

	if b == 0:
		return 1
	elif b>a:
		return 0
	else:
		return recurs_f(a-1, b) + recurs_f(a-1, b-1)

n, k = map(int, input().split())
y = recurs_f(n, k)
print(y)
