# Iterables

# Iterable - list, dictionary, tuple, set, string, a collection of items
# They can all be iterated on
# We can go one by one to check each item in the collection

user = {
	'name' : "Golem",
	'age' : 5006,
	'can_swim' : False
}

# prints the keys of the dictionary
for item in user.items():
	print(item)

print()
# prints the values of the dictionary
# for item in user:
# 	print(user[item])

for item in user.values():
	print(item)

print()
# prints the key-value pairs
for item in user.items():
	print(item)

print()
# formatted print the key-value pairs
for key, value in user.items():
	print(key, value)

print()
# print over numbers
for item in range(50):
	print(item)