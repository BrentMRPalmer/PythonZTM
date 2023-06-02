# Exercise: Pokedex JPG to PNG Converter

# Give the program 2 arguments
# 1) The folder
# 2) The new folder to create

import sys
import os
from PIL import Image

# Grab the first and second argument
source = sys.argv[1]
target = sys.argv[2]

# Check if new/ exists, if not create it
if not os.path.isdir(target):
	os.mkdir(target)

# Loop through Pokedex
for file in os.listdir(source):
	# Convert images to png
	image_path = os.path.join(source, file)
	img = Image.open(image_path)
	file = file[:-4] + '.png'

	# Save them to the new folder
	save_path = os.path.join(target, file)
	img.save(save_path, 'PNG')

