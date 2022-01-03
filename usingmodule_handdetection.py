import cv2
import mediapipe as mp
import time
import handtractingmodule as htm


pTime = 0 #Previos time is 0
cTime = 0 #Current Time is 0
cap = cv2.VideoCapture(0)
# 1 is the camera setting
detector = htm.handDetector()

while True:
    success, img = cap.read()
    img = detector.findHands(img, draw=False)
    lmList = detector.findPosition(img,draw=False)
    if len(lmList) != 0:
        print(lmList[4])
    # FPS Algo
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    # Displaying FPS on the screen
    cv2.putText(img, "FPS: " + str(int(fps)), (18, 78), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)
    cv2.putText(img,"Made by: Anvesh Dange", (18,150), cv2.FONT_HERSHEY_PLAIN, 2, (0,255, 0), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)