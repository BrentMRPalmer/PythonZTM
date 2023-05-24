# Generators
# Generators allow us to generate a sequence of values over time.
# range(100) is an example of a generator

# range is a generator, so it is not being held in memory
# It does not create a list 
# It gives one number at a time
range(100)

list(range(100)) # basically the same as make_list function

def make_list(num):
	result = []
	for i in range(num):
		result.append(i * 2)
	return result

# my_list points to a location in memory
my_list = make_list(100)
print(my_list)

# This would take lots of space in memory
print(list(range(1000000)))