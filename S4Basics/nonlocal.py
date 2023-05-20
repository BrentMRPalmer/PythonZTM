# Nonlocal

def outer():
	x = "local"
	def inner():
		nonlocal x # I do not want to use new local x - take from parent
		x = "nonlocal"
		print("Inner: ", x)
	inner()
	print("Outer: ", x)

outer()