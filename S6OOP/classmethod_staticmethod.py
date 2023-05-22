# Class Methods and Static Methods

class PlayerCharacter:
	membership = True
	def __init__(self, name, age):
		self.name = name 
		self.age = age

	def shout(self):
		print(f"My name is {self.name}") 

	@classmethod
	def adding_things(cls, num1, num2): # cls is kind of like self, but do not need to have instance of class
		return cls("Teddy", num1 + num2) # Instantiates the class

	@staticmethod 
	def subtracting_things(num1, num2): # we do not have access to cls
		return num1 - num2

player1 = PlayerCharacter("Brent", 21)

player3 = PlayerCharacter.adding_things(2,3) # class method since it doesn't need an instance of the class
print(player3.name)

print(player3.subtracting_things(5,4))
