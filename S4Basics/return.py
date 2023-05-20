# Return
# Function: should do one thing really well
# Should often return something

def sum(num1, num2):
	def another_func(n1, n2):
		return n1 + n2
	return another_func(num1, num2)

def sum2(my_list):
	new_int = 0
	for number in my_list:
		new_int += number
	my_list.append(new_int)

print(sum(10, 20))

a = [1,2,3]
sum2(a)
print(a)