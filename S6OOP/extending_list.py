# Extending List

class SuperList(list):
	def __len__(self):
		return 1000


super_list = SuperList([1,2,3,4])

print(len(super_list))
super_list.append(5)
print(super_list)
print(super_list[2])
print(len(super_list))

print(issubclass(SuperList, list)) # True because SuperList is a subclass of list
print(issubclass(list, object)) # True since everything is an object