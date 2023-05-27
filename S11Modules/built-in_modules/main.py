import random
# from random import shuffle
# import random as oulala # (aliasing)

import sys

print(random)

# help(random)

# print(dir(random)) shows all the available methods

# print(random.random()) # Random number between 0 and 1
# print(random.randint(1,10)) # Random number between 1 and 10
# print(random.choice([1,2,3,4,5])) # Picks a random element from the list
my_list = [1,2,3,4,5]
random.shuffle(my_list)
# print(my_list)

print(sys)
first = sys.argv[1]
last = sys.argv[2]
print(f"Hello {first} {last}")
