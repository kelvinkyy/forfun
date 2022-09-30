import os
from PIL import Image
import numpy as np
import cv2
import pickle

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR,"images")

current =0
label_id={}
y_label = []
x_train = []

face_cascade = cv2.CascadeClassifier("C:/Users/kelvi/PycharmProjects/For_Fun/cascades/data/haarcascade_frontalface_alt.xml")
recognizer = cv2.face.LBPHFaceRecognizer_create()

for root,dirs,files in os.walk(image_dir):
    for file in files:
        if file.endswith("png") or file.endswith("jpg"):
            path = os.path.join(root, file)
            label = os.path.basename(os.path.dirname(path)).replace(" ","-").lower()
            #print(label, path)
            pil_image = Image.open(path).convert("L")
            image_array = np.array(pil_image,"uint8")
            if not label in label_id:
                label_id[label] = current
                current = current + 1

            id = label_id[label]
            #print(label_id)

            #print(image_array)
            faces = face_cascade.detectMultiScale(image_array, scaleFactor=1.01, minNeighbors=5)

            for(x,y,w,h) in faces:
                roi = image_array[y:y+h, x:x+w]
                x_train.append(roi)
                y_label.append(id)

#print(y_label)
#print(x_train)

with open("labels.pickle", "wb") as f:
    pickle.dump(label_id,f)

recognizer.train(x_train, np.array(y_label))
acc = recognizer.score(np.array(y_label))
print(acc)
recognizer.save("trainner.yml")