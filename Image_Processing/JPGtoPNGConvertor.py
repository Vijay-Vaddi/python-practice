import os
import sys
from PIL import Image

path = './'

# grab source and destination 
source, destination = sys.argv[1], sys.argv[2]
source = path+source
destination = path+destination
# check if new folder exists, if not create it
os.makedirs(destination, exist_ok=True)
directory = os.fsencode(source)

# loop through the pokedex
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    print(filename)
    if filename.endswith(".jpg") or filename.endswith(".jpeg"): 
        # convert 
        name, exten = os.path.splitext(filename)
        img = Image.open(source+'/'+filename)
        # save to new folder
        img.save(destination +'/'+name+'.png', 'png')
        # img.save(os.path.join(destination, name), 'png')
    else:
        continue
