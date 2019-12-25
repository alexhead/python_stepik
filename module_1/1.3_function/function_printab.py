def printab(a, b): # возможная запись аргументов по умолчанию
	print(a)		# printab(a, b=10)
	print(b)

#correct ways to call a function

printab(10, 20)
printab(a=10, b=20)

#keyword arguments always after non-keyword arguments
printab(10, b=20)

lst = [10, 20]
printab(*lst) # = printab(lst[0], lst[1])

args = {'a':10, 'b':20}
printab(**args) # = printab(key1=args[key1], key2=args[key2])

