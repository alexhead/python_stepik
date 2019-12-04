class MoneyBox:
	def __init__(self, capacity):
		self.capacity = capacity

	def can_add(self, v):
		if (self.capacity - v) > 0:
			return True
		else:
			return False

	def add(self, v):
		if x == True:
			self.capacity = self.capacity + v
			print('yes')
		else:
			self.capacity = self.capacity
			print(self.capacity)

a = MoneyBox(10)
x = a.can_add(5)
y = a.add(5)