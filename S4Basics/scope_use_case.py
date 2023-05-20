# Why do we need scope?
# Computers do not have infinite memory
# Scope is great for memory management

def outer(): # Once a function is done, it destroys the memory - efficient
	x = "local"
	def inner():
		nonlocal x
		x = "nonlocal"
		print("Inner: ", x)
	inner()
	print("Outer: ", x)

outer() # running this creates a location in memory of scope of functions

My-var = 5
print(My-var)