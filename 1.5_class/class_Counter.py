class Counter:
	def __init__(self, start=0):
		self.count = 0

Counter # class object
x1 = Counter(10)
x = Counter()
print(x.count) #0
x.count += 1