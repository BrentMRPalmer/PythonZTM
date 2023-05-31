# File Paths

# This is called a relative path (because it is relative to pwd)
with open(r'app\sad.txt', mode='r') as my_file:
	text = my_file.read()
	print(text) 

# Writing the entire path is called the absolute path
# The r is for "raw string" that does not recognize \
with open(r'C:\Season6\PythonZTM\S13FileIO\app\sad.txt', mode='r') as my_file:
	text = my_file.read()
	print(text) 

# Sometimes there is a .\ which also means from the current folder (.. goes back one)
with open(r'.\app\sad.txt', mode='r') as my_file:
	text = my_file.read()
	print(text) 

# Pathlib is a built-in library that can be used
# such that it works on both mac and windows