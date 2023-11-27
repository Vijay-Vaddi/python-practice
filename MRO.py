# Method Resolution Order
# pythons rule on which method to run when having multiple inheritances among classes

class A:
    num = 10

class B(A):
    pass

class C(A):
    num = 1

class D(B,C):
    pass

print(D.num)
print(D.mro())

class X:pass
class Y: pass
class Z:pass
class A(X,Y):pass
class B(Y,Z):pass
class M(B,A,Z):pass
# due to depth first search implementation of MRO implementation X comes to A first, then Y comes to A.   
print(M.mro())