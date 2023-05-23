# Zip
# Returns a list of tuples of the ith elements of each list
# First item from each in a tuple, second item from each in a tuple, ... ,
# and nth item from each in a tuple

my_list = [1, 2, 3, 4, 5]
your_list = [10, 20, 30, 40, 50]
their_list = [100, 200, 300, 400, 500]

print(list(zip(my_list, your_list, their_list)))