# Question 5 

# Define a class which has at least two methods:

# inputString: Implement a method called getString that prompts the user to enter a string and returns the input obtained from the console.
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

class StringProcess:
	def __init__(self, my_string = ""):
		self.my_string = my_string

	def inputString(self):
		self.my_string = input("Enter the string you would like to process: ")

	def printString(self):
		print(self.my_string.upper())

def test():
	processor = StringProcess("Test")
	processor.printString()
	processor.inputString()
	processor.printString()

test()