class D: pass
class E: pass
class B(D, E): pass
class C: pass
class A(B, C): pass

print(issubclass(A, A)) # True
issubclass(C, D) # False
issubclass(A, D) # True
issubclass(C, object) #True
issubclass(object, C) #False

