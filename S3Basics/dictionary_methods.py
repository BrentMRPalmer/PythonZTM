# Dictionary Methods

user = {
	'basket' : [1,2,3],
	'greet' : 'Hello',
	'age' : 77
}

print(user.get('age', 55)) # checks if the argument is a valid key - 55 is a default if it doesn't exist

user2 = dict(name = 'Brent')
print(user2)

print('basket' in user)
print('greet' in user.keys())
print('Hello' in user.values())

print(user.keys())
user2 = user.copy()
user.clear()
print(user)
print(user2)
print(user2.pop('age'))
print(user2)
user2.update({'age':22})
print(user2)
user2.update({'age':33})
print(user2)

# Exercise 

#Scroll down to see the answers!
#1 Create a user profile for your new game. This user profile will be stored in a dictionary with keys: 'age', 'username', 'weapons', 'is_active' and 'clan'

print("EXERCISE")

user_profile = {
	'age' : 21,
	'username' : 'Dawn',
	'weapons' : ['axe', 'spear'],
	'is_active' : True,
	'clan' : 'Versus'
}

#2 iterate and print all the keys in the above user.

print(user_profile.keys())

#3 Add a new weapon to your user

user_profile['weapons'].append('colt')
print(user_profile["weapons"])

#4 Add a new key to include 'is_banned'. Set it to false


user_profile.setdefault("is_banned", False)
print(user_profile.keys())
print(user_profile["is_banned"])

#5 Ban the user by setting the previous key to True

user_profile["is_banned"] = True
print(user_profile["is_banned"])

#6 create a new user2 my copying the previous user and update the age value and username value.

user2 = user_profile.copy()
user2.update({"age" : 20, "username" : "Death"})
print(user2)
