import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))

class LoggableList(list, Loggable):
	def append(self, tex):
		self.log(tex)
		x = len(self)
		self.insert(x, tex)
x = LoggableList()
x.append('as')
x.append('1')
x.append('1')
x.append('2')
x.append('as')
x.append('2')
print(x)
