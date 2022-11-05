import cv2
import numpy as np
import csv
import time
import pygame

from sklearn import svm
import pandas as pd

cap = cv2.VideoCapture(0)
img = cap.set(cv2.CAP_PROP_FRAME_WIDTH,480)
img = cap.set(cv2.CAP_PROP_FRAME_HEIGHT,360)

#Database: Gerbang LOgika AND
#Membaca data dari file
FileDB = 'warna_text.txt'
Database = pd.read_csv(FileDB, sep=" ", header=0)
print(Database)

#x = Data, y=Target
x = Database[[u'B', u'G', u'R']]
y = Database.Target

#Training and Classify
clf = svm.SVC()
clf.fit(x,y)

fpsLimit = 1            #throttle limit
startTime = time.time()

while True:
    ret, img = cap.read()
    #cv2.regtangle(img,(300,220),       (340,260),      (0,0,255),3)
    img = cv2.flip(img,1)           #untuk membalikkan kamera yang terbalik
    for x in range (330,340,1):
        for y in range (220,260,1):
            color = img[x,y]
            colorB = img[y,x,0]
            colorG = img[y,x,1]
            colorR = img[y,x,2]

    print('B G R = ', color)
    cv2.imshow("Color Tracking", img)

    if clf.predict([color]) == 'BIRU':
        print("BIRU")

    elif clf.predict([color]) == 'HIJAU':
        print("HIJAU")
        file = 'hijau.wav'
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        time.sleep(3)

    elif clf.predict([color]) == 'KUNING':
        print("KUNING")

    elif clf.predict([color]) == 'MERAH':
        print("MERAH")
        file = 'merah.wav'
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        time.sleep(3)

    elif clf.predict([color]) == 'PUTIH':
        print("PUTIH")
        file = 'putih.wav'
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        time.sleep(3)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
        
