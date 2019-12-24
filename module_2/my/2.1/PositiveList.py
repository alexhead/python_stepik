
class PositiveList(list):
    def append(self, x):
        try:
            if x > 0:
                super().append(x)

x = PositiveList()

x.append(-1)

print(x)