# Dictionary
# Keys must be immutable
# A key cannot be a list

x = 5

dictionary = {
	123 : [1,2,3],
	123 : [5,6,7], # overwrites the first value with key 123
	True : 'Hello',
	x : 'Dan'
}

print(dictionary[123])