import cv2
import pickle

#img = cv2.imread('img2.jpeg')

width, height =  80, 575

try:
   with open('ImgSlot', 'rb') as f:
        posList = pickle.load(f)
         
except:
    posList = []
    

def mouseClick(events,x,y,flags,params):
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x, y))
    if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            x1,y1 = pos
            if x1 < x < x1 + width and y1 < y < y1 + height:
                posList.pop(i)

    with open('ImgSlot', 'wb') as f:
         pickle.dump(posList, f)
                

while True:
  #  cv2.rectangle(img,(130,580),(50,5),(255,0,255),2) # for img width and height set
    img = cv2.imread(r"H:\tray_solt_image\image\img2.jpeg")
    for pos in posList:
        cv2.rectangle(img, pos, (pos[0]+width, pos[1]+height),(255,0,255),2)
  
    cv2.imshow("image",img)
    cv2.setMouseCallback("image",mouseClick)
    cv2.waitKey(1)

