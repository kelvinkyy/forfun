import cv2
import mediapipe as mp
import time
import math

#opening camera 1
cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

cTime = 0
pTime = 0

#if it the camera cannot open the process will end
if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    #return true to success if it reads, returning the frame to img
    success, img = cap.read()
    #flip the image 180 because it just makes more sense to me
    img = cv2.flip(img,180)

    #changing the colour i guess??? idk why
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                print(id,lm)
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                if id == 0:
                    cv2.circle(img, (cx,cy), 30, (255,0,255),cv2.FILLED)
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    cv2.putText(img,str(math.floor(fps)), (10,70),cv2.FONT_HERSHEY_PLAIN, 3,(66,245,69), 3)

    #displaying the images(video)
    cv2.imshow("Image",img)
    #press "q" to exit or just end the process to exit
    if cv2.waitKey(1) == ord('q'):
        break
#release so it doesnt take up memory
cap.release()
cv2.destroyAllWindows()