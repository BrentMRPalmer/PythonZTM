# Decorators 3

# Decorator Pattern (using *args and **kawrgs)
def my_decorator(func):
	def wrap_func(*args, **kwargs):
		func(*args, **kwargs)
	return wrap_func

@my_decorator
def hello(greeting, emoji=':)'):
	print(greeting, emoji)

hello("Hello")

# a = my_decorator(hello)
# a("Hello")