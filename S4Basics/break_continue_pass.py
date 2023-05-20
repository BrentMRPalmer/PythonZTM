# Break, continue, and pass

my_list = [1,2,3]

# Break: exit entire loop
for item in my_list:
	print(item)
	break

i = 0
while i < len(my_list):
	print(my_list[i])
	i += 1
	break

# Continue: exit current iteration
for item in my_list:
	if item % 2 == 0: 
		continue
	print(item)

i = 0
while i < len(my_list):
	print(my_list[i])
	i += 1
	continue

# Pass: does nothing - good for a placeholder
for item in my_list:
	#thinking about it
	pass
	
i = 0
while i < len(my_list):
	print(my_list[i])
	i += 1
	pass