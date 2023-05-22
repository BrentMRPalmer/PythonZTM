# Encapsulation

# Four pillars of OOP
# 1) Encapsulation: The binding of data and functions
#                   that manipulate that data into 
#                   one big object that can be used.
#                   It hides complexity.

class PlayerCharacter: # Without methods, it is basically the same as a dictionary
	def __init__(self, name, age):
		self.name = name 
		self.age = age

player1 = PlayerCharacter("Brent", 21)
print(player1.name)
print(player1.age)

player2 = {"name": "Brent", "age" : 21}
print(player2['name'])
print(player2['age'])