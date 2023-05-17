# List Patterns

basket = ['a', 'x', 'b', 'c', 'd', 'e', 'd']
basket.sort()
basket.reverse()
print(basket[::-1])
print(basket)

print(list(range(1,100)))

sentence = ' '
new_sentence = sentence.join(['hi', 'my', 'name', 'is', 'Brent'])
print(new_sentence)

# Exercise

#fix this code so that it prints a sorted list of all of our friends (alphabetical). Scroll to see answer
friends = ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', 'Chu']

new_friend = ['Stanley']

print( sorted((friends + new_friend)) )