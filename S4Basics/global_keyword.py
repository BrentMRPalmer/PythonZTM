# Global keyword

total = 0

# def count():
# 	global total 
# 	total += 1
# 	return total

# Dependency injection is better than using global

def count(total):
	total += 1
	return total

print(count(count(count(total))))