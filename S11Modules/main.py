# Main

# we do not add the .py, as we assume we are importing a python file
import utility
# creates a compiled file for utility and stores it in __pycache__
# using a compiled file makes things faster (the essence of caching)

print(utility)
# printing the module will show the path to the module

print(utility.multiply(1,2))
# using a function from utility module
