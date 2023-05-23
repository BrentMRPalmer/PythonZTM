# Error Handling 2

def sum(num1, num2):
	try:
		return num1 + num2
	except TypeError as err:
		print(f"Please enter numbers. {err}")

def div(num1, num2):
	try:
		return num1 / num2
	except (TypeError, ZeroDivisionError) as err:
		print(err)


print(sum('1', 2))
print(div(1, '2'))