# Walrus Operator

a = "Hello000000000000"

if ((n := len(a)) > 10):
	print(f"Too long, {n} elements")

while (n := len(a)) > 1:
	print(n)
	a = a[:-1]