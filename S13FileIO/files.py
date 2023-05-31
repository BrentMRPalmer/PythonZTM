# Working With Files in Python
# File IO
# Input, Output

# I want you to input something from the outside world,
# and output something to the outside world
# (you being the computer)

# Python has built-in for opening files

my_file = open('test.txt')
print(my_file.read()) # Reads the file
print(my_file.read()) # The contents of the file are read by a cursor
print(my_file.read()) # Cursor cannot move back on its own - is at end of file, so it doesn't reread
my_file.seek(0) # Use seek to move cursor
print(my_file.read())

my_file.seek(0)
print(my_file.readline()) # Reads only one line
print(my_file.readline())
print(my_file.readline())

my_file.seek(0)
print(my_file.readlines()) # Creates a list of all lines

# Must manually close the file after opening it
my_file.close()