
def fib(x):
	if x == 0 or x ==1: # базовый случай
		return 1
	else:
		return fib(x-1) + fib(x-2) # вызов самой себя до наступления базового случая

y = fib(int(input()))
print(y)