# Abstraction

# Four pillars of OOP
# 2) Abstraction: Hiding of information, and giving access
#                 to only what is necessary. 

# This makes our coding more efficient
# We do not need to learn everything from scratch

class PlayerCharacter:
	def __init__(self, name, age):
		self.name = name 
		self.age = age

	def run(self):
		print("Run") 

	def speak(self):
		print(f"My name is {self.name}, and I am {self.age} years old.")

player1 = PlayerCharacter("Brent", 21)
player1.speak() 
# This is abstraction in action
# When we click run, we get a string from speak
# However, we do not know how speak is implemented
# This is exactly what abstraction is

print((1,2,3).count(2)) # This is abstraction because we don't know (or need to know) how count is implemented.
print(len((1,2,3,4))) # This is also abstraction for the same reason

player1.name = "!!!"
player1.speak = "BOOOO"
# print(player1.speak()) # Does not work because speak has been modified to be a string attribute
print(player1.speak)