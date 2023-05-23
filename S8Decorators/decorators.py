# Decorators
# @name
# Decorators "supercharge" our functions
# By adding a decorator, we can add extra
# functionality to our functions

# Examples
# @classmethod
# @staticmethod

# Functions are first-class in Python
# That means that they can be passed as arguments in functions
# Functions are basically just variables in Python


def hello():
	print("Hello")

def hello2(func): # Functions can be passed as variables
	func()

def greet():
	print("Still here")

def greet2():
	def func():
		return "Greetings"
	return func

greet = hello
del hello # just deletes the name reference, not the instructions

greet()

hello2(greet)

# Higher Order Functions (HOC)
# 1) A function that accepts another function (like hello2) (also map, filter, reduce, zip)
# 2) It is a function that returns another function (like greet2) 


