# -*- coding: utf-8 -*-

from PIL import Image
import glob
import os
import pillow_avif

#define path of folder with webp
fold_path = "filepath"

#change current working dir
try:
    os.chdir(fold_path)
except:
    print("No such folder path")
    exit(0)


#get a list of names of images in the webp path
im_names = glob.glob("*")

#create a new folder in the curr working directory
os.mkdir(fold_path + "jpg")


for i in im_names:
    print(i)
    
count = 1
#loop through each img file
for i in im_names:
    curr_im = Image.open(i).convert("RGB")
    #save image in new directory as jpeg
    curr_im.save(fold_path + "jpg//" + str(count) + ".jpg", "jpeg")
    count += 1
    curr_im.close()



