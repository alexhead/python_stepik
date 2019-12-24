from itertools import takewhile
import itertools

def primes():
    a = 1
    while True:
        a += 1
        k = 1
        s = 0
        for i in range(a):
            b = a / k
            if a % k == 0:
                s += 1
            k += 1
        if s == 2:
            yield a


print(list(itertools.takewhile(lambda x: x <= 31, primes())))