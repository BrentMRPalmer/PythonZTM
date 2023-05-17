# Built-in functions and methods

# Built-in Functions
# Functions are independent from the class
# function()

# len()
# Finds the length of a string
greet = 'hello';
print(len(greet))
print(greet[0:len(greet)])

# Built-in Methods
# Act on a specific class
# class.method()

quote = "to be or not to be"
print(quote.upper())
print(quote.capitalize())
print(quote.lower())
print(quote.find('be'))
print(quote.replace('be', 'die'))
print(quote)

quote2 = quote.replace('be', 'die')
print(quote2)