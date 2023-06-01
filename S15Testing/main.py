# Main 

def do_stuff(num=0):
	try:
		if num is not None:
			return int(num) + 5
		else:
			return 'Please Enter Number'
	except ValueError as err:
		return err