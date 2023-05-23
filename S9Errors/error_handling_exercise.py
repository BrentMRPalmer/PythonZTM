# Error Handling Exercise

while True:
	try:
		age = int(input("Enter is your age: "))
		10/age
	except ValueError: # Only the first except block that catches an error will run
		print("Please enter a number")
		continue
	except ZeroDivisionError:
		print("Please enter an age higher than 0")
		break
	else: # If there is no error, run this
		print("Thank you!")
		break
	finally:
		print("Ok, I am finally done.")
	print("Can you hear me")