# Images 2

from PIL import Image, ImageFilter

img = Image.open(r'.\Pokedex\pikachu.jpg')
converted_img = img.convert('L')
# converted_img.show()
# crooked = converted_img.rotate(90)
# crooked.save("grey.png", "png")

# resize = converted_img.resize((300,300))
# resize.save("resized.png", "png")

box = (100, 100, 400, 400)
crop = converted_img.crop((box))
crop.save("crop.png", "png")