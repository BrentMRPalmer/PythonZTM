# Ask for username
username = input('Enter your username: ')
# Ask for password
password = input('Enter your password: ')

secret = '*' * len(password)

print(f"{username}, your password {secret} is {len(password)} letters long")

