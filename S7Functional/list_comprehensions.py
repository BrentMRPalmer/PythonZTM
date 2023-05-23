# List Comprehensions

# Comprehensions: A quick way to create list or sets or dictionaries in Python
# instead of looping or appending
# Shorthand form for list creation

# Old technique
my_list = []

for char in "Hello":
	my_list.append(char)

print(my_list)

# List Comprehension Technique
# General List Comprehensions Format 
# list_comprehension = [expression for param in iterable]

my_list2 = [char for char in "Hello"]
print(my_list2)

my_list3 = [number for number in range(101)]
print(my_list3)

my_list4 = [2 * number for number in range(101)]
print(my_list4)

my_list5 = [number**2 for number in range(101) if number**2 % 2 == 0]
print(my_list5)