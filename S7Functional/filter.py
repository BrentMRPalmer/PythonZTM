# Filter
# Runs first parameter (function) on each element on iterable
# Only saves elements that the function returns True on

my_list = [1, 2, 3, 4, 5]

def check_odd(element):
	return element % 2 == 1

print(list(filter(check_odd, my_list)))