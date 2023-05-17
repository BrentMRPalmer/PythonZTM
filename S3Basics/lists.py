# Lists
# An ordered sequence of objects of any length

li = [1, 2, 3, 4, 5]
li2 = ['a', 'b', 'c']
li3 = [1, 2, 'a', True]

# Data Structure
# A way to organize data
# A container around your data that has different pros and cons

amazon_cart = ['notebooks', 'sunglasses']
print(amazon_cart[0])

# Exercise

#What is the output of this code?
#Before you click RUN, guess the output of each print statement!
new_list = ['a', 'b', 'c']
print(new_list[1])
# b
print(new_list[-2])
# b
print(new_list[1:3])
# ['b', 'c']
new_list[0] = 'z'
print(new_list)
# ['z', 'b', 'c']

my_list = [1,2,3]
bonus = my_list + [5]
my_list[0] = 'z'
print(my_list)
# ['z', 2, 3]
print(bonus)
[1, 2, 3, 5]