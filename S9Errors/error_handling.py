# Error Handling
# Allows the script to continue running, even if there is an error


while True:
	try:
		age = int(input("Enter is your age: "))
		10/age
	except ValueError: # Only the first except block that catches an error will run
		print("Please enter a number")
	except ValueError:  # this will not run
		print("!!!!")
	except ZeroDivisionError:
		print("Please enter an age higher than 0")
	else: # If there is no error, run this
		print("Thank you!")
		break

