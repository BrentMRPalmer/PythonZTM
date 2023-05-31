# File IO Errors

try: 
	with open('test.txt', mode='r') as my_file:
		print(my_file.read())
except IOError as err: # Can use the more specific FileNotFoundError
	print('file does not exist')
	raise err