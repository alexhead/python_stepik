
def divide(x, y): 
	try:
		result = x / y
	except ZeroDivisionError:
		print("division by zero")
	else:
		print("result is", result)
	finally:
		print("finaly")

divide(2, 1)
divide(2, 0)
divide(2, [])