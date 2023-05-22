# Private Versus Public

# Private variables? No true private variable (not as simple as private int x like in Python)
class PlayerCharacter:
	def __init__(self, name, age):
		self._name = name # use underscore for private
		self._age = age # does not actually do anything, but it is a generally understood convention

	def run(self):
		print("Run") 

	def speak(self):
		print(f"My name is {self._name}, and I am {self._age} years old.")

player1 = PlayerCharacter("Brent", 21)

player1._name = "!!!"
player1.speak = "BOOOO"

print(player1.speak)