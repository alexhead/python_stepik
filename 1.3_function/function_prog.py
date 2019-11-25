
def closest_mod_5(x):
	if x%5 == 0:
		y = x
		
	else:
		while x%5 != 0:
			x+=1
		y = x
	print(y)
	return y	
	 


x = int(input())
closest_mod_5(x)
