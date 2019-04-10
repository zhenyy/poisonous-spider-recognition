from PIL import Image
import os
import cv2
import numpy as np
import glob
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
root_path = r"C:\\Users\\vincent916735\\Desktop\\Img"
print(root_path)
path_save = "C:\\Users\\vincent916735\\Desktop\\Img_resized"
dir = root_path
count = 0
for root,dir,files in os.walk(dir):
    for file in files:
        srcImg = cv2.imread(root_path+"\\"+str(file))
        img = Image.open(root_path+"\\"+str(file))
        print(root_path+str(file))
        newImg = img.resize((600, 600),Image.ANTIALIAS)
        newImg.save(os.path.join(path_save,os.path.basename(str(count)+'.jpg')))
        count+=1
