# Lambda Exercise

# Create a one line lambda expression that will print a squared list

my_list = [5,4,3]

print(list(map(lambda item: item * item, my_list)))

# List Sorting - Sort by second value in tuples
a = [(0,2), (4,3), (9,9), (10,-1)]

a.sort(key = lambda x: x[1])
print(a)