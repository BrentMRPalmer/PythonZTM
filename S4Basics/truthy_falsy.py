# Truthy and Falsy

print(bool("Hello")) # Truthy
print(bool(5)) # Truthy
print(bool("")) # Falsy
print(bool(0)) # Falsy

# Example: just making sure each field has any value
username = 'johnny'
password = '123'

if password and username:
	print("Form complete")