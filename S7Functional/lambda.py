# Lambda expressions
# One-time anonymous functions
# Useful for tasks that do not need to be repeated
# Since they are only used once, they do not need a name
# nor do they need to be stored

from functools import reduce

# lambda parameter: action(param)

my_list = [1,2,3]

print(list(map(lambda item: item * 2, my_list)))
print(list(filter(lambda item: item % 2 == 1, my_list)))
print(reduce(lambda acc, item: acc + item, my_list))