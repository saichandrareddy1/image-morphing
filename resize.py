import os
from PIL import Image

path = os.path.abspath("./images")
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
            print("HII")
            im = im.resize((600, 600),Image.ANTIALIAS)
            im.save(r"C:\Users\Sai Chandra Reddy\Desktop\Crickters\new images\0000"+str(s)+".jpg")
        except IOError:
            print("Bye")
            print ("cannot create thumbnail for '%s'" % i)
