from PIL import Image, ImageFilter
import os

img = Image.open('./Image_Processing/pokedex/pikachu.jpg')

os.makedirs('./Image_Processing/pokedex/process_images/', exist_ok=True)
processed_image_dir_path = './Image_Processing/pokedex/process_images/'

# print(img)
# print(dir(img)) #all ops that can be done on img object
# print(img.format)
# print(img.size)
# print(img.mode)

#blurs the file
filtered_image = img.filter(ImageFilter.BLUR)
filtered_image.save('blur.png', 'png')

#smoothen
filtered_image2 = img.filter(ImageFilter.SMOOTH)
filtered_image2.save('smoothened.jpeg', 'jpeg')

# coverts to grey scale
filtered_image3 = img.convert('L')
filtered_image3.save('grey.png', 'png')

#opens in a window
filtered_image3.show()

#rotate and show
filtered_image3.rotate(90).show()

#resize
filtered_image4 = filtered_image3.resize((300,300))
filtered_image4.save('resized.png', 'png')
new_path = processed_image_dir_path+'resized.png'
#find better way to auto save files into a new dir. 
filtered_image4.save(new_path, 'png')

filtered_image4.show()

# crop

box = (100,100,400,400)
cropped_image = filtered_image4.crop(box)
cropped_image.save(new_path+'cropped.png', 'png' )
 

