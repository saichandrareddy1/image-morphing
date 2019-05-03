# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 09:48:51 2019

@author: Sai Chandra Reddy
"""

import cv2
from keras.models import load_model
import numpy as np


emotions = ['angry', 'disgusted', 'fearful','happy', 'sad', 'surprised', 'neutral']
cascade_classifier = cv2.CascadeClassifier(r"D:\Ubuntu\data\haarcascade_frontalface_default.xml")
model = load_model(r'face.hdf5')
model.summary()


def face_predict(face, gray):
    gray = gray[face[1]:(face[1] + face[2]), face[0]:(face[0] + face[3])]
    try:
        gray = cv2.resize(gray, (64, 64), interpolation=cv2.INTER_CUBIC) / 255.
        gray = np.expand_dims(gray, axis=-1)
        gray = np.expand_dims(gray, axis= 0)
    except Exception:
        print("Problem during resize")
        return None
    result = model.predict(gray)
    return result


if __name__ == '__main__':
    
    image = cv2.imread(r"D:\Ubuntu\data\fear.jpg")

    if len(image.shape) > 2 and image.shape[2] == 3:
        print("HII")
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray = cv2.imencode(image, cv2.IMREAD_GRAYSCALE)

    faces = cascade_classifier.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5)
    
for face in faces:
    (x, y, w, h) = face
    cv2.rectangle(image, (x,y), (x+w,y+h), (255,0,0), 2)
    print(x, y, w, h)
    result = face_predict(face, gray)
    text = emotions[np.argmax(result[0])]
    print(result, text)
    cv2.putText(image, text, (x, y), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
print(emotions)

cv2.imshow('happy.jpg', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('detected_faces.png', image)