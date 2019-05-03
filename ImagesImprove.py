# -*- coding: utf-8 -*-
"""
Created on Wed May  1 00:11:14 2019

@author: Sai Chandra Reddy
"""

import os
from PIL import Image
import cv2
#import numpy as np

path = r"D:\Ubuntu\Backup\images\Test\sai"
def getlist(path):
  """Returns a list of filenames for
    all jpg images in a directory. """
  lis = [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg') or f.endswith('.jpeg')]
  return lis
c = getlist(path)

s = 0
for i in c:
    s += 1
    if i.endswith('.jpg') or i.endswith('.jpeg'):
        try:
            print("HII")
            color = cv2.imread(i)
            gray = cv2.cvtColor(color, cv2.COLOR_RGB2GRAY)
            img = Image.fromarray(gray)
            img.save(r"D:\Ubuntu\Backup\images\newimages\image"+str(s+100)+".jpg")
            
            #####FLIP####
            flip = cv2.flip(color, 1)
            flip = Image.fromarray(flip)
            flip.save(r"D:\Ubuntu\Backup\images\newimages\flipimage"+str(s+100)+".jpg")
            
            #####Rotate#######
            rotate = cv2.rotate(color, 1)
            rotate = Image.fromarray(rotate)
            rotate.save(r"D:\Ubuntu\Backup\images\newimages\rotateimage"+str(s+100)+".jpg")
            
            ###Masking the images######
            ret, mask = cv2.threshold(color, 175, 200, cv2.THRESH_BINARY_INV)
            mask = Image.fromarray(mask)
            mask.save(r"D:\Ubuntu\Backup\images\newimages\maskimage"+str(s+100)+".jpg")
            
            ####Edges#######
            #edge = cv2.Laplacian()
            
            
        except IOError:
            print("Bye")
            print ("cannot create thumbnail for '%s'" % i)
