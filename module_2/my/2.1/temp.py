class NonPositiveError(Exception):
    pass

class PositiveList(list):

    def append(self, x):
        if x > 0:
            super().append(x)
        else:
            raise NonPositiveError

x = PositiveList()

x.append(-11)
x.append(3)
x.append(-3)
x.append(3)

print(x)