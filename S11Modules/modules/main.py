# Main Packages
# A package is a folder that contains modules
# NOTE: When you import a file it runs it

# from shopping import shopping_cart
from shopping import utility
# max will overwrite existing functions

# import shopping.more_shopping.shopping_cart
# from shopping.more_shopping import *
# from shopping.more_shopping.shopping_cart import buy

from shopping.more_shopping import shopping_cart
# good to prevent name collision (ex: max above)

print(shopping_cart.buy("Dog"))
print(utility.multiply(1,2))

print(max([1,2,3]))

print(__name__) # the file that is run is always 'main'
                # even if it has a different name

if __name__ == '__main__':
    # Code that we only want to run if it is the file that is
    # explicitly run
    print("Please run this")

print(type(utility.st1))

