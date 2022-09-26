import cv2
import pickle
import cvzone
import numpy as np

#video or img Read

cap = cv2.VideoCapture(r"H:\tray_solt_image\image\carPark.mp4")

while True:
    success, img = cap.read()
    cv2.imshow("Image", img)
    cv2.waitKey(30)