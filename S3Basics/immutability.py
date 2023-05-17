# Slicing
example = "dog"
example2 = example[1:3]
print(example2)

# Immutability
example = 100
print(example)
# You can fully overwrite
example = "dog"
# example[0] = "a" not possible since strings are immutable (cannot change one element of the string)
print(example)