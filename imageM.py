import cv2
import mediapipe as mp
import numpy as np
from PIL import Image

p_y8=0
p_y4=0
pxy8=0
pxy4=0
pxx8=0
pxx4=0
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
mhand= mp.solutions.hands
hands=mhand.Hands()
currentH=620
currentW=480
logo = cv2.imread(r"C:\Users\waleed\PycharmProjects\hands\download (15).png")
size = 100
logo = cv2.resize(logo, (size, size))
img2gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)

while True:
    _, image =cap.read()
    height, width, channels = image.shape
    imgConverted = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    result =hands.process(image=imgConverted)
    if result.multi_hand_landmarks:
        for handL in result.multi_hand_landmarks:
            for id, lo in enumerate(handL.landmark):
                if id == 8:
                    pxy8 = -int(lo.y * height)
                    pxx8 = -int(lo.x * width)

            ret, mask = cv2.threshold(img2gray, 1, 255, cv2.THRESH_BINARY)
            roi = image[-size-pxy8:-pxy8, -size-pxx8:-pxx8]
            try:
                roi[np.where(mask)] = 0
                roi += logo
            except:
                print()

    cv2.imshow('my webcam',image)
    cv2.waitKey(1)