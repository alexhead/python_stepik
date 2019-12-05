class MoneyBox:
	def __init__(self, capacity):
		self.count = 0
		self.capacity = capacity

	def can_add(self, v):
		if (self.capacity - self.count - v) >= 0:
			return True
		else:
			return False

	def add(self, v):
		if self.can_add(v) == True:
			self.count = self.count + v
		else:
			return False

	def print_box(self):
		print(self.count)


a = MoneyBox(10)
a.can_add(5)
a.add(5)
a.print_box()
a.can_add(4)
a.add(4)
a.print_box()



