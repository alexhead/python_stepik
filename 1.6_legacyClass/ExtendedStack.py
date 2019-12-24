class ExtendedStack(list):
	def sum(self): # сумма
		a = 0
		for i in range(2): 
			a += self.pop()
		self.append(a) 
		return self

	def sub(self):
		a = self.pop() - self.pop()	
		self.append(a)
		return self

	def mul(self):
		a = self.pop() * self.pop()
		self.append(a)
		return self

	def div(self):
		a = self.pop() // self.pop()
		self.append(a)
		return self
	

lis = ExtendedStack([1, 2, 5, 10, 2])


print(lis.sum())

print(lis.sub())

