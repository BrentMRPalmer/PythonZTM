# How to Debug Code

# The act of finding and removing bugs and errors 
# from code is called "debugging"

# Linting
# Detects issues with code as we go
# Extensions that notice issues 

# IDE or Editor
# These IDEs have built-in tools that we can use
# such as autoformatting based on PEP-8
# Highlighting is very useful

# Reading Errors
# Understanding how to read errors is very important
# in being able to resolve them

# PDB
# Python Debugger
# This is a built-in module in Python

import pdb

def add(num1, num2):
	pdb.set_trace()
	4 + 5
	return num1 + num2

add(4, 'kjfdhghjd')

# PDB
# pdb.set_trace() pauses code
# Pauses code - interactive debugger
# Can type num1 to check what's in num1
# help to view available functions
# help [function] to receive documentation
# step is used to go to the next line
# continue interpets code until it returns something
# a gives all the arguments of the current function
# w shows the context of the current line (which function, with what arguments)
# exit to leave the pdb debugger mode
# you can change the values of variables during pdb mode