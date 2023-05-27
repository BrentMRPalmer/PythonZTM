# Useful Modules 2

import datetime

print(datetime.time(5,45,2))
print(datetime.date.today())

from array import array

# What is an array?
# Lists in Python are sometimes called arrays in other languages, but they are a bit different
# Lists in Python are what we call dynamic - anytime we need data we can make it as big as we want
# Arrays, however, take up less memory since they are statically sized (we must choose the memory used in advance)

# array(typecode, )
arr = array('i', [1,2,3])
print(arr[0])