import cv2
import os
import numpy
from PIL import Image

def RGBTOGRAY(path, new_path):
    i = 0
    for img in os.listdir(path):
        try:
            if img is not None:
                i = i+1
                color = cv2.imread(path+img, cv2.IMREAD_COLOR)
                img = cv2.cvtColor(color, cv2.COLOR_BGR2GRAY)
                image = img * 255
                cv2.imwrite(new_path + str(i+1) +".png", image)
                print("INFO[] Image is COnverted...."+str(path + os.listdir(path)[i-1]))
            else:
                print("sorry")
        except Exception:
            print("INFO [] REGARDING Exception", Exception)


data_train = input("Enter the training data folder***")
data_test = input("enter the testing data folder***")
MaskTrain = input("Enter the ***Masking*** Train data folder***")
MaskTest = input("Enter the ***Masking*** Test data folder***")

ls = [data_train, data_test, MaskTrain, MaskTest]
for i in range(len(ls)//2):
    if i == 0:
        path = os.path.join(os.getcwd(), ls[0] + '/' + ls[2] + '/')
        new_path = ("/home/saireddy/Research/Data/data_train/masktrain/image")
        RGBTOGRAY(path , new_path)
        print("===============================DONE CONVERTED=============================")
    elif i == 1:
        path = os.path.join(os.getcwd(), ls[1] + '/' + ls[3] + '/')
        new_path = ("/home/saireddy/Research/Data/data_test/masktest/image")
        RGBTOGRAY(path , new_path)
        print("===============================DONE CONVERTED=============================")
    else:
        print("INFO[] SORRY SOMETHING WENT WRONG............................")

