# Init

class PlayerCharacter:
	# Class Object Attribute
	membership = True # Shouldn't change across different instances
	def __init__(self, name='Anonymous', age=0): # default values
		if(age > 18):
			self.name = name #attributes
			self.age = age

	def shout(self):
		print(f"My name is {self.name}") # Must use self.attribute for instance attributes


player1 = PlayerCharacter('Tom', 10) # Will not instantiate attributes since underage
print(player1)

# player1.shout()