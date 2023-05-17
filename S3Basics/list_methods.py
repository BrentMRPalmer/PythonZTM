# List Methods

basket = [1,2,3,4,5]
print(basket[1:])

# Adding
basket.append(6)
new_list = basket.append(7) # append does not return anything - changes in-place

print(basket)
print(new_list)

basket.insert(3, 100)
print(basket)

basket.extend([102, 200])
print(basket)

# Removing
top = basket.pop()
basket.pop(0)
basket.remove(100)
print(basket)
print(top)

basket.clear()
print(basket)

basket = [1,2,3,4,5,3]
print(basket.index(2, 0, 3))
print(3 in basket)
print(basket.count(3))

# Exercises
# using this list, 
basket = ["Banana", "Apples", "Oranges", "Blueberries"];

# 1. Remove the Banana from the list

basket.pop(0)
print(basket)

# 2. Remove "Blueberries" from the list.

basket.pop(2)
print(basket)

# 3. Put "Kiwi" at the end of the list.

basket.append("Kiwi")
print(basket)

# 4. Add "Apples" at the beginning of the list

basket.insert(0, "Apples")
print(basket)

# 5. Count how many apples in the basket

print(basket.count("Apples"))

# 6. empty the basket

basket.clear()
print(basket)

# End of exercise

basket = [5,2,4,3,1]
x = sorted(basket)
y = basket.copy() # same as basket[:]
basket.reverse()
print(basket)
print(x)
basket.sort()
print(basket)
