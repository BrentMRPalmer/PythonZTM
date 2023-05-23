# Reduce

# This is like in Prolog
# Reduces an iterable to a single value
# Accumulates using an accumulator
# Does an operation to add each element to the accumulator

# Import the reduce function
from functools import reduce 

my_list = [1,2,3]
my_list2 = ["Hello, ", "have a nice ", "day"]

def accumulator(acc, item):
	return acc + item

print(reduce(accumulator, my_list, 0)) # Third argument is initial value of acc
print(reduce(accumulator, my_list2, "Welcome! "))