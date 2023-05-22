# Creating Our Own Objects
# Classes are great for DRY (do not repeat yourself)

class PlayerCharacter:
	# __init__ method is used as a constructor method / init method
	# the two underlines means "dunder method" or "magic method"
	# this is used whenever we instantiate an object of the class
	# first parameter of class methods is always self
	# self refers to the object to the left of the dot (my_string.len())
	def __init__(self, name, age):
		self.name = name # These are called the attributes of the class
		self.age = age

	def run(self):
		print("Run!")
		return "Done"

# player1 = PlayerCharacter() # This does not work because we are not giving a name argument
player1 = PlayerCharacter("Brent", 21)
player2 = PlayerCharacter("Sarah", 20)

print(player1)
print(player2)
print(player1.name)
print(player2.name)
print(player1.age)
print(player2.age)
print(player1.run())

player2.attack = 50
print(player2.attack) # Creates attribute at runtime
# print(player1.attack)