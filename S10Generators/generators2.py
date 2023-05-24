# Generators 2

# Iterable: any object in Python which we are able to loop through
# Iterate: the act of taking an item from an iterable, doing something with it, and going to the next one
# It has the __iter__ dunder method implemented
# Generators are iterable
# Everything that is a generator is iterable, but not everything that is iterable is a generator

# Generator is a subset of an iterable

# How to make a generator

# yield pauses the function and comes back to it later
# give i, and when you tell me to keep going I'll keep going

def generator_function(num):
	for i in range(num):
		yield i * 2

g = generator_function(100)

print(g)
print(next(g))
print(next(g))
print(next(g)) # Works like iterator in Java

# for item in generator_function(1000):
# 	print(item)

# Old technique

# def make_list(num):
# 	result = []
# 	for i in range(num):
# 		result.append(i)
# 	return result