# Tuples
# Data Structure
# Essentially immutable lists
# Instead of [] they use ()

my_tuple = (1,2,3,4,5)
print(my_tuple)
print(my_tuple[1])
print(5 in my_tuple)

user = {
	'basket' : [1,2,3],
	'greet' : 'hello',
	'age' : 20,
	(1,2) : 'Death'
}

print(user.items()) # returns a couple for each key:value pair
print(user[(1,2)])

# Tuples 2

my_tuple = (1,2,3,4,5)
new_tuple = my_tuple[1:4]
x,y,z, *rest = (1,2,3,4,5,1)
print(rest)

print(my_tuple.count(1))
print(my_tuple.index(5))