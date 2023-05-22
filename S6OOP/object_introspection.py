# Object Introspection
# Introspection refers to the ability to determine
# the type of an object at runtime
# Runtime: when the code is running

class User():
	def __init__(self, email):
		self.email = email

	def sign_in(self):
		print("Logged in")

class Wizard(User):
	def __init__(self, name, power, email):
		User.__init__(self, email)
		self.name = name
		self.power = power

	def attack(self):
		User.attack(self) # Can use the parent method this way
		print(f"Attacking with power of {self.power}")

class Archer(User):
	def __init__(self, name, num_arrows, email):
		# User.__init__(self, email)
		super().__init__(email) # works the same as commented line
		self.name = name
		self.num_arrows = num_arrows

	def attack(self):
		print(f"Attacking with arrows. Arrows left: {self.num_arrows}")

# Introspection
wizard = Wizard("Merlin", 50, "merlin@gmail.com")
print(dir(wizard)) # dir function gives all methods and attributes of the object