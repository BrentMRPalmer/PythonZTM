# Error Handling 3
# As a programmer, you must anticipate and handle errors.

while True:
	try:
		age = int(input("Enter is your age: "))
		10/age
		raise ValueError("Hey, cut it out!")
	except ZeroDivisionError:
		print("Please enter an age higher than 0")
		break
	else: # If there is no error, run this
		print("Thank you!")
		break
	finally:
		print("Ok, I am finally done.")
	print("Can you hear me")