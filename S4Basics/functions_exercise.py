# Functions Exercise

def highest_even(li):
	highest = 0
	for number in li:
		if number % 2 == 0 and number > highest:
			highest = number
	return highest

def highest_even2(li):
	evens = []
	for item in li:
		if item % 2 == 0:
			evens.append(item)
	return max(evens)

print(highest_even2([10,2,3,4,8,11]))