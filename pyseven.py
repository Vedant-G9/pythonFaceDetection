import cv2

faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")## trained model

img = cv2.imread('Resources/img.png')##-----------------------------------------source of the image
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)##-------------------------------we need gray scale image to detect the faces

faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)##-------------------------Faces are detected

for(x, y, w, h) in faces:##-----------------------------------------------------this loop will run for all the faces detected
    cv2.rectangle(img, (x, y), (x+w, y+h), (150,0,0),3)
    #print(x,y)


cv2.imshow('output', img)
cv2.waitKey(0)
