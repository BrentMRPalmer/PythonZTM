# While

# i = 0
# while i < 50:
# 	print(i)
# 	i += 1
# else: # could be useful in a situation where break is used (only executes if no break)
# 	print("Done with all the work.")

my_list = [1,2,3]

for item in my_list:
	print(item)

i = 0
while i < len(my_list):
	print(my_list[i])
	i += 1

i = 0
while True:
	response = input("Say something: ")
	if response == "bye":
		break
