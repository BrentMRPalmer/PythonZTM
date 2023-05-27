# Useful Modules (built-in)

# Collection module

from collections import Counter, defaultdict, OrderedDict

li = [1,2,3,4,5,6,7,7]
sentence = "This is a great example sentence!"

# Counter
# Counter makes a counter object that keeps track of how many times
# each object occurs in an iterable
# (Similar to a dictionary)
# Output is in order of frequency. 
print(Counter(li))
print(Counter(sentence))

# defaultdict
# Gives a default value if indexed using a non-existent key
dictionary = defaultdict(lambda: 5, {'a' : 1, 'b' : 2})
print(dictionary['c'])

# OrderedDict
# Retains the order of insertions into the dictionary

d = {}
# d = OrderedDict()
d['a'] = 1
d['b'] = 2

d2 = {}
# d2 = OrderedDict()
d2['a'] = 1
d2['b'] = 2

# A normal dictionary does not have order (this would be true)
# Note: This was changed in Python 3.7 - now they have order
print(d2 == d)
