def s(a, *vs, b=10):
   res = a + b
   for v in vs:
       res += v
   print(res)

s(0, 0, 31)