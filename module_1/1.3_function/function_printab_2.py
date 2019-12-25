# передача множества аргументов
def printab(a, b, *args):
	print("positional argument a ", a)
	print("positional argument b ", b)
	print("additional arguments:")
	for arg in args:
		print(arg)
def printab_kwargs(a, b, **kwargs):
	print("positional argument a ", a)
	print("positional argument b ", b)
	print("additional arguments:")
	for key in kwargs:
		print(key, kwargs[key])


printab(10, 20, 30, 40, 50)
# positional argument a 10
# positional argument b 20
# additional arguments
# 30
# 40 
# 50
printab_kwargs(10, 20, c=30, d=40, jimi=123)

