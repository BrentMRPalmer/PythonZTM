# Pure Functions

# Functions that always output the same given the same input
# Two rules
# 1) Given the same input, it will always return the same output
# 2) A function should not produce any side effects

# Pure functions entail less buggy code
# Pure functions is more of a "guideline" than an absolute - sometimes it is necessary

# new_list = [] # If new_list was defined here, the function would not be pure (interactions with outside world)
# If new_list were changed to a string, for exampple, it would crash
# This is a good reason to make functions pure - it can prevent errors

# Functional Programming approach to wizad
wizard = {
	"name" : "Merlin",
	"power" : 50
}

# Separate functions instead of methods

def attack(character):
	print("Attack")

# This is a pure function
def multiply_by2(li):
	new_list = []
	for item in li:
		new_list.append(item*2)
	return new_list # If this was a print, it would not be a pure function (impacts the display)


print(multiply_by2([1,2,3]))