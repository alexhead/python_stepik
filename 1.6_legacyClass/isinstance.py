class D: pass
class E: pass
class B(D, E): pass
class C: pass
class A(B, C): pass

x = A()
isinstance(x, A) # True
isinstance(x, B) # True
isinstance(x, object) # True
isinstance(x, str) # False