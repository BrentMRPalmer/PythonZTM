# Attributes and Methods

class PlayerCharacter:
	# Class Object Attribute
	membership = True # Shouldn't change across different instances
	def __init__(self, name, age):
		if(PlayerCharacter.membership):
			self.name = name 
			self.age = age

	def shout(self):
		print(f"My name is {self.name}") # Must use self.attribute for instance attributes

player1 = PlayerCharacter("Brent", 21)
player2 = PlayerCharacter("Sarah", 20)

player2.attack = 50
player1.shout()
print(PlayerCharacter.membership) # Since membership is a class object attribute