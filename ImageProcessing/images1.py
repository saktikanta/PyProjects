from  PIL import Image, ImageFilter

img = Image.open('./astro.jpg')

# print(img.size)
# new_img = img.resize((400, 400))
# new_img.save("thumbnail.jpg")

img.thumbnail((400, 200))
img.save("thumbnail.jpg")
print(img.size)

# filtered_img = img.filter(ImageFilter.BLUR)
# filtered_img.save("blur.png", 'png')
# filtered_img = img.convert('L')
# filtered_img.save("gray.png", 'png')
# print(dir(img))
# filtered_img.show()

# crooked = filtered_img.rotate(270)
# crooked.save("gray.png", 'png')

# resize = filtered_img.resize((200, 200))
# resize.save("gray.png", 'png')

# box = (100, 100, 400, 400)
# region = filtered_img.crop(box)
# region.save("gray.png", 'png')
