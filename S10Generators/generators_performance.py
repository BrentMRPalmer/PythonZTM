# Generators Performance

from time import time

def gen_fun(num):
	for i in range(num):
		yield i

def performance(func):
	def wrapper(*args, **kwargs):
		start = time()
		result = func(*args, **kwargs)
		end = time()
		print(f'It took {end-start} ms')
		return result
	return wrapper

@performance
def long_time():
	print('1')
	for i in range(100000000):
		i*5

@performance
def long_time2():
	print('2')
	for i in list(range(100000000)):
		i * 5

long_time() # It took 7.529443264007568 ms
long_time2() # It took 11.614217519760132 ms