# Fibonacci Numbers
# using generators


def fibonacci_generator(n):
	if n == 0: 
		yield 0
	if n > 0: 
		yield 0
		yield 1
	prev = 0
	current = 1
	for i in range(1, n):
		temp = current
		current += prev
		prev = temp
		yield current

for element in fibonacci_generator(10000):
	print(element)


# SOLUTION 
def fib(number):
	a = 0
	b = 1
	for i in range(number + 1):
		yield a
		temp = a
		a = b 
		b = temp + b

# for element in fib(20):
# 	print(element)

def fib2(number):
	a = 0
	b = 1
	result = []
	for i in range(number):
		result.append(a)
		temp = a
		a = b 
		b = temp + b
	return result

# print(fib2(10000))