
def divide(x, y): 
	try:
		result = x / y
	except:
		print("Error")
	finally:
		print("finaly")

for i in range(5):
	divide(int(input()), int(input()))
