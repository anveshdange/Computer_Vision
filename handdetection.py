import cv2
import mediapipe as mp
import time
print("All modules imported succesfully")

cap = cv2.VideoCapture(0)
# 1 is the camera setting

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0 #Previos time is 0
cTime = 0 #Current Time is 0



while True:
    success, img = cap.read()
    # Converting to RGB Image
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    print(results.multi_hand_landmarks)

    # If else statements
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                # print(id,lm)
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                # print(id,  cx, cy)
                # Coloring our pointers ...
                # if id == 4:
                #     cv2.circle(img, (cx, cy), 25, (255, 0, 255), cv2.FILLED)


            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    # FPS Algo
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    # Displaying FPS on the screen
    cv2.putText(img, "FPS: " + str(int(fps)), (18, 78), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)
    cv2.putText(img,"Made by: Anvesh Dange", (18,150), cv2.FONT_HERSHEY_PLAIN, 2, (0,255, 0), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
