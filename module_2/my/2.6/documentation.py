import sys

class RandomPlus:
    """
    .plus - sum x and y
    .creep - return x

    """

    def creep(x):
        return x

    def plus(x, y):
        print(x + y)

print(RandomPlus.__doc__)

RandomPlus.plus(int(input("Введите X")), int(input("Введите Y")))

print(sys.__doc__)

