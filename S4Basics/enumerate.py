# Enumerate

for i, character in enumerate("Hello"):
	print(i, character)

for i, char, in enumerate(list(range(100))):
	if char == 50:
		print(i, char)