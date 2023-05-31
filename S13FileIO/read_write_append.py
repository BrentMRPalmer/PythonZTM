# Read, Write, Append

# Better way to do file IO with Python
# Don't need to worry about closing afterwards
# Mode 'r' means read, and the default mode is 'r'
# with open('test.txt', mode='r') as my_file:
# 	print(my_file.readlines())

# Mode 'w' means write
with open('test.txt', mode='w') as my_file:
	text = my_file.write("Hey it's me!") # Overwrites the file entirely (assumes new file)
	print(text) 

# Mode 'r+' means read and write 
# with open('test.txt', mode='r+') as my_file:
# 	text = my_file.write("Hey it's me!") # It returns the number of characters it writes
# 	print(text) # Also, when we write it overwrites the existing text

# Mode 'a' means append
# with open('test.txt', mode='a') as my_file:
# 	text = my_file.write("Hey it's me!") # Adds to end of file
# 	print(text) 