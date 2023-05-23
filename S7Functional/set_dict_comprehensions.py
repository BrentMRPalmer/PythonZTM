# Set and Dictionary Comprehensions

my_set = set()

for char in "Hello":
	my_set.add(char)

# print(my_set)

# Set Comprehension Technique
# General Set Comprehensions Format 
# set_comprehension = {expression for param in iterable}

my_set2 = {char for char in "Hello"}
# print(my_set2)

my_set3 = {number for number in range(101)}
# print(my_set3)

my_set4 = {2 * number for number in range(101)}
# print(my_set4)

my_set5 = {number**2 for number in range(101) if number**2 % 2 == 0}
# print(my_set5)

# Dictionary Comprehension Technique

simple_dict = {
	'a' : 1,
	'b' : 2
}

my_dict = {key:value**2 for key,value in simple_dict.items() if value % 2 == 0}
print(my_dict)

my_dict2 = {num:num*2 for num in [1,2,3]}
print(my_dict2)

