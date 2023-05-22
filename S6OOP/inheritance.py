# Inheritance

# Pillars of OOP
# 3) Inheritance: Allows new classes to take on the
#                 properties of old classes

# Users
	# Wizards
	# Archers
	# Ogres

# All the different types of users all need to be able to sign in

# No need for init since it will be inherited
# This class only has methods
class User():
	def sign_in(self):
		print("Logged in")

class Wizard(User):
	def __init__(self, name, power):
		self.name = name
		self.power = power

	def attack(self):
		print(f"Attacking with power of {self.power}")

class Archer(User):
	def __init__(self, name, num_arrows):
		self.name = name
		self.num_arrows = num_arrows

	def attack(self):
		print(f"Attacking with arrows. Arrows left: {self.num_arrows}")

wizard = Wizard("Merlin", 50)
archer = Archer("Robin", 100)

wizard.sign_in() # The wizard inherits the functionality of the user class
archer.sign_in() # As does the archer

# Same method name, but they function differently
wizard.attack() 
archer.attack()

# Inheritance 2

print(isinstance(wizard, Wizard))
print(isinstance(wizard, User))
print(isinstance(wizard, Archer))
print(isinstance(wizard, object)) # Everything in Python is an object