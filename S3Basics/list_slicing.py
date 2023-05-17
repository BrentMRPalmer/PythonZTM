# List slicing
# Lists are mutable
amazon_cart = [
	'notebooks',
	'sunglasses',
	'toys',
	'grapes'
]
amazon_cart[0] = 'laptop'
new_cart = amazon_cart # Python has aliasing
new_cart = amazon_cart[:] # This creates a copy of the list
new_cart[0] = 'gum'

print(new_cart)
print(amazon_cart)