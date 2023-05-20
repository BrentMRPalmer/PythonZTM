# is versus ==
# == evaluates the expressions (checks for equality in value)
#	will convert the types (sometimes)
# is checks if the location in memory is the same
# 	will not convert the types

print(True == 1)
print('1' == 1)
print([] == 1)
print(10 == 10.0)
print([] == [])

print(True is 1)
print('1' is 1)
print([] is 1)
print(10 is 10.0)
print([] is []) # Two different lists in different places in memory
print(True is True)

a = 534336
b = 534336
print(a is b)

a = [1,2,3]
b = [1,2,3]
print(a is b)
b = a
print(a is b)