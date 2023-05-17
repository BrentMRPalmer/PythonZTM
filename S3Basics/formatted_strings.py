# Formatted strings

name = 'John'
age = 55

print(f"Hello {name}. You are {age} years old.")
print( "Hello {0}. You are {1} years old.".format(name, str(age)) )
print( "Hello {name2}. You are {age2} years old.".format(name2 = 'Bob', age2 = 54) )

# Exercises
# 1 What would be the output of the below 4 print statements? 
# Try to answer these before you click RUN!

print("Hello {}, your balance is {}.".format("Cindy", 50))
# Hello Condy, your balance is 50.

print("Hello {0}, your balance is {1}.".format("Cindy", 50))
# Hello Cindy, your balance is 50.

print("Hello {name}, your balance is {amount}.".format(name="Cindy", amount=50))
# Hello Cindy, your balance is 50. 

print("Hello {0}, your balance is {amount}.".format("Cindy", amount=50))
# Hello Cindy, your balance is 50. 

# 2 How would you write this using f-string? (Scroll down for answer)

name = 'Cindy'
amount = 50
print(f"Hello {name}, your balance is {amount}.")