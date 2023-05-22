# Dunder Methods

class Toy():
	def __init__(self, colour, age):
		self.colour = colour
		self.age = age
		self.my_dict = {
			'name' : 'Yoyo',
			'has_pets' : False
		}

	def __str__(self): # Only modified for the Toy class
		return f'{self.colour}'

	def __len__(self):
		return 5

	def __call__(self):
		return('yes??') # This is what calling it will do

	def __getitem__(self, i):
		return self.my_dict[i]

	def __repr__(self):
		return f'Toy("{self.colour}", {self.age})'

	def __bool__(self):
		return self.colour == "Red"

	def __eq__(self, other):
		return self.colour == other.colour and self.age == other.age

action_figure = Toy("Red", 0)
hotwheels = Toy("Red", 0)

print(action_figure.__str__())
print(str(action_figure))
print(len(action_figure))
print(action_figure())
print(action_figure['has_pets'])
print(repr(action_figure))
print(bool(action_figure))
print(action_figure == hotwheels)

