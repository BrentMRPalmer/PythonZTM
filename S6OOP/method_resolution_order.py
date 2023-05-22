# MRO - Method Resolution Order
# A rule that Python follows to decide which method to run

class A:
	num = 10

class B(A):
	pass

class C(A):
	num = 1

class D(B, C):
	pass

print(D.num)
print(D.mro())

# 	 A 
#  /   \ 
# B     C
#  \   /
#    D
# MRO: D, B, C, A

# Process: What's first in line? What should I pick? Check order using D.mro()
# The general process is that it checks itself, then immediate parent, then the parent of parent, etc.
# If it has two parents, 

class X: pass
class Y: pass
class Z: pass
class A(X,Y): pass
class B(Y,Z): pass
class M(B,A,Z): pass

print(M.mro()) # MRO uses DFS