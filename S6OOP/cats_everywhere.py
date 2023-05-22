# Cats Everywhere

# Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 1 Instantiate the Cat class with 3 cats

cat1 = Cat("Mark", 5)
cat2 = Cat("Stacy", 20)
cat3 = Cat("Dipdip", 13)

# 2 Create a function that finds the age of the oldest cat
# NOTE: FUNCTION, not method! Takes class as input!

def age_of_oldest(*cats):
	return max(cats)

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2

print(f"The oldest cat is {age_of_oldest(cat1.age, cat2.age, cat3.age)} years old. ")