# *Args and **Kwargs

# Can accept any number of arguments as a tuple
# **kward -> keyword arguments
# does not need to be called "args" or "kwargs", but it is convention
def super_func(name, *args, age = 0, **kwargs):
	print(kwargs)
	total = 0
	for items in kwargs.values():
		total += items
	return sum(args) + total

print(super_func("Brent", 1,2,3,4,5, num1=5, num2=10))

# Rule: params, *args, default parameters, **kwargs