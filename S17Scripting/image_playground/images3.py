# Images 3

from PIL import Image, ImageFilter

img = Image.open(r'.\astro.jpg')

# new_img = img.resize((400,400)) # Lost some aspect ratio
img.thumbnail((400,400)) # Keeps aspect ratio
img.save("thumbnail.jpg")

print(img.size)