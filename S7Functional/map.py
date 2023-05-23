# Map
# Applies the function to each item in the iterable
my_list = [1,2,3]

def multiply_by2(element):
	return element * 2

map(multiply_by2, my_list)
print(my_list) # Map does not impact my_list (pure function)