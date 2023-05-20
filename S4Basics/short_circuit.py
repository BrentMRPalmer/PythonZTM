# Short circuiting

is_friend = True
is_user = True

# Short circuiting is the idea that with
# or, once one condition is true it doesn't
# bother checking the rest - can 
# improve runtime or avoid errors
# Another example: In and, once one condition
# is false it short circuits
if is_friend or is_user:
	print("Best friends forever")