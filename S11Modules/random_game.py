# Random Game

# Generate a number lower-upper

# Input from user?

# Check that input is a number lower-upper

# Check if the number is the right guess. Otherwise ask again. 

import random
import sys

lower = int(sys.argv[1])
upper = int(sys.argv[2])

number = random.randint(lower, upper)
guess = lower - 1

while guess != number:
	try:
		guess = int(input(f"Guess the number between {lower} and {upper}: "))
		if guess < lower or guess > upper:
			print("Guess out of bounds. Please try again.")
			continue
		if guess == number:
			print(f"Congratulations on guessing the number {number}")
		else:
			print("Incorrect guess. Try again.")
	except:
		print("Not an integer. Try Again. ")
	