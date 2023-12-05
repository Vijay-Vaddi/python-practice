# images from unsplash.com
from PIL import Image, ImageFilter

img = Image.open('./Image_Processing/astro.jpg')
new_img = img.resize((400,400))
new_img.save('./Image_Processing/processed_images/resized.jpg')
#resize doesn't keep the aspect ratio. 

#thumnail keeps aspect ratio. Max value is 400x400. 
# output size may not be the same. 
#used for creating profile pics 

img.thumbnail((400, 400))
img.save('./Image_Processing/processed_images/thumbnail.jpg')
print(img.size)
