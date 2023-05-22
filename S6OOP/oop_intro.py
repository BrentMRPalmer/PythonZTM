# OOP
# OOP is a paradigm, which is a way for us to think
# about and structure our code in a way that is easier
# to maintain, extend, and write. 

# Everything in Python is an object
# Everything is built using class keyword

# We can use the class keyword to create our own classes

print(type(None))
print(type(True))
print(type(5))
print(type(5.5))
print(type('hi'))
print(type([]))
print(type(()))
print(type({}))

# As code gets bigger and bigger it becomes millions of
# lines of code divided into different files
# Programming something like a drone is very complicated
# OOP creates modularity and makes things more manageable

# OOP is a paradigm, which is a way for us to think
# about and structure our code in a way that is easier
# to maintain, extend, and write. 

# Break things up into small pieces, based on objects
# which represent things in the real world

# Ex:
# Drone would have different classes for
# propellers, signal processing, camera, etc.
# Allows for different people to work on different parts. 
# May be able to reuse classes for different projects.

# What is OOP? Part 2

# Definition of a new class
class BigObject: # Class 
	# Code
	pass

# The class is the blueprint
# What are the basic attributes?
# What are the basic methods?

# Can instantiate instances of objects using the blueprint

obj1 = BigObject() # Instantiation

print(type(obj1))