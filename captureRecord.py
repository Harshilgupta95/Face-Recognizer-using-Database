import cv2
import numpy as np
import sqlite3
import os

conn=sqlite3.connect('Database.db')
if not os.path.exists('./Dataset'):
    os.makedirs('./Dataset')
c=conn.cursor()
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap=cv2.VideoCapture(0)
uname=input("Enter Your Name: ")
c.execute('INSERT INTO User1 (Name) VALUES (?)',(uname,))
uid=c.lastrowid
samplenum=0
while True:
    ret,img=cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        samplenum=samplenum+1
        cv2.imwrite("Dataset/User."+str(uid)+"."+str(samplenum)+".jpg",gray[y:y+h,x:x+w])
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.waitKey(100)
    cv2.imshow('img',img)
    cv2.waitKey(1);
    if samplenum>=20:
        break
print('\n Samples Captured Successfully')
cap.release()
conn.commit()
conn.close()
cv2.destroyAllWindows()
