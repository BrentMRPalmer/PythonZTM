# Multiple Inheritance 

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

	def check_arrows(self):
		print(f"Attacking with arrows. Arrows left: {self.num_arrows}")

	def run(self):
		print("Ran really fast")

# Multiple inheritance - can give as many parameters as we want
class HybridBorg(Wizard, Archer): # Inherited from Wizard first, then Archer - uses Wizard constructor (if init not overridden)
	def __init__(self, name, power, arrows):
		Archer.__init__(self, name, arrows)
		Wizard.__init__(self, name, power)

hybrid_borg = HybridBorg("Lina", 100, 200)
hybrid_borg.run()
hybrid_borg.attack()
hybrid_borg.check_arrows()
hybrid_borg.sign_in()



