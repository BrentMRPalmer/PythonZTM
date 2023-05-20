# Scope - what variables do I have access to?

# total = 100
# if defined here it would be part of the 
# global scope of the file

def some_func():
	total = 100

# print(total) 
# total is only in the scope of the function

if True:
	x = 10 
print(x)
# new scope is not created from an if statement