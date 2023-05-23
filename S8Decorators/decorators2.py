# Decorators 2
# A decorator superchargers a function
# It is a function that wraps another function that enhances it
# Python uses @ to recogniaze a wrapper

# Since it accepts another function, it is a higher-order function
def my_decorator(func):
	def wrap_func():
		print("*****")
		func()
		print("*****")
	return wrap_func

# @my_decorator
def hello():
	print("Hello")

@my_decorator
def bye():
	print("Bye")

# hello()
# bye()

# This is how it works
hello2 = my_decorator(hello)
hello2()
# or my_decorator(hello)()