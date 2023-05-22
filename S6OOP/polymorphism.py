# Polymorphism

# Pillars of OOP

# 4) Polymorphism: Poly means many, and morphism means form
#                  Methods belong to objects, so polymorhphism
#                  refers to the way object classes can share
#                  the same method names, but the same
#                  name can act differently. 

class User():
	def sign_in(self):
		print("Logged in")

	def attack(self): # This will be overridden
		print("Do nothing.")

class Wizard(User):
	def __init__(self, name, power):
		self.name = name
		self.power = power

	def attack(self):
		User.attack(self) # Can use the parent method this way
		print(f"Attacking with power of {self.power}")

class Archer(User):
	def __init__(self, name, num_arrows):
		self.name = name
		self.num_arrows = num_arrows

	def attack(self):
		print(f"Attacking with arrows. Arrows left: {self.num_arrows}")

wizard = Wizard("Merlin", 50)
archer = Archer("Robin", 100)

# Same method name, but they function differently - this is polymorphism
print("Example 1: ")
wizard.attack() 
archer.attack()
print()


# Can use the same method name, but they work differently (even though we are calling the "same thing")
print("Example 2:")
def player_attack(char):
	char.attack()

player_attack(wizard)
player_attack(archer)
print()

# A third example of polymorphism
print("Example 3:")
for char in [wizard, archer]:
	char.attack()
print()