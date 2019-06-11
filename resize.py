from PIL import Image
from imutils import paths
import requests
import cv2
import os


path = os.path.abspath(r"C:\Users\Sai Chandra Reddy\Desktop\Sports Vision\YellowCards")
def get_imlist(path):
  """Returns a list of filenames for
    all jpg images in a directory. """
  lis = [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg')]
  return lis
c = get_imlist(path)

s = 0
for i in c:
    s +=1
    if i.endswith('.jpg'):
        try:
            im = Image.open(i)
            im = im.resize((600, 600),Image.ANTIALIAS)
            im.save(r"C:\Users\Sai Chandra Reddy\Desktop\Sports Vision Resized\NewYellowcards\0000"+str(s)+".jpg")
        except IOError:
            print ("cannot create thumbnail for '%s'" % i)

for imagePath in paths.list_images(r"C:\Users\Sai Chandra Reddy\Desktop\Sports Vision Resized\NewYellowcards"):
  
  delete = False
  
  try:
    image = cv2.imread(imagePath)
    
    if image is None:
      delete = True
      
  except:
    print("Except")
    delete = True
        
  if delete:
    print("[INFO] deleting {}".format(imagePath))
    os.remove(imagePath)
