import numpy
import cv2
import pickle

face_cascade = cv2.CascadeClassifier("C:/Users/kelvi/PycharmProjects/For_Fun/cascades/data/haarcascade_frontalface_alt.xml")
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainner.yml")

label = {"person detected":1}
with open("labels.pickle", "rb") as f:
    og_label = pickle.load(f)
    label = {v:k for k,v in og_label.items()}


cap = cv2.VideoCapture(0)

while True:

    success, img = cap.read()

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(imgGray, scaleFactor = 1.01, minNeighbors = 5)

    for(x,y,w,h) in faces:
        
        roi_imgGray = imgGray[y:y+h, x:x+w]
        roi_img = img[y:y + h, x:x + w]

        id, loss = recognizer.predict(roi_imgGray)
        if loss > 50:
            print("UNCLASSIFIED")
        else:
            print(id)
            print(label[id])
        img_item = "test_image.png"
        cv2.imwrite(img_item, roi_imgGray)

        cv2.rectangle(img, (x,y),(x+w, y+h), (255,0,255), 2)
    if not success:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    cv2.imshow("Image", img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()