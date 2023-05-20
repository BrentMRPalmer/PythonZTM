# Default Parameters and Keyword Arguments

# positional parameters (because the position matters)
# default parameters: setting a value if nothing is given
def say_hello(name = "Darth Vader", emoji = ">:)"):
	print(f"Hello {name} {emoji}")

# positional arguments (because the position matters)
say_hello("Brent", ":)")

# keyword arguments
say_hello(emoji = ':)', name = 'Bob')

say_hello()
say_hello(emoji = ":(")
say_hello("Bob")