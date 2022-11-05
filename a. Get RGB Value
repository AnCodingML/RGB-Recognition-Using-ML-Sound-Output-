import cv2
import numpy as np
import csv
import time

cap = cv2.VideoCapture(0)

while True:
    ret,img =cap.read()
    #cv2.regtangle(img,(300,220),       (340,260),(0,0,255),3)
    for x in range (330,340,1):
        for y in range(220,260,1):
            color = img[x,y]
            colorB = img [y,x,0]
            colorG = img[y,x,1]
            colorR = img[y,x,2]
    #print(color, 'WHITE')
    cv2.imshow('Pengambilan Database', img)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
