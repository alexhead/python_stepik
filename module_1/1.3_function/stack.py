# Стек вызовов

def g():
	print("I am in function g")

def f():
	print("I am in function f")
	g()
	print("I am in function f")

print("I am outside of any function")
f()
print("I am outside of any function")
