import cv2
import pickle
import cvzone
import numpy as np

#video or img Read

cap = cv2.VideoCapture(r"H:\tray_solt_image\image\video1.mp4")

with open('ImgSlot', 'rb') as f:
        posList = pickle.load(f)

width, height =  80, 575

while True:


    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES,0)
    success, img = cap.read()    

    for pos in posList:
        cv2.rectangle(img, pos, (pos[0]+width, pos[1]+height),(255,0,255),2)    

    
    cv2.imshow("Image", img)
    cv2.waitKey(10)