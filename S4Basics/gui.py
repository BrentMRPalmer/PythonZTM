# GUI

#Exercise!
#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

for row in picture:
	my_string = ""
	for element in row:
		if element == 0:
			my_string += " "
		elif element == 1:
			my_string += "*"
	print(my_string)

# instead of making an alternate string you can
# also use print("*", end = "")

