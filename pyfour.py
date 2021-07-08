import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
print(img)

imgDraw=cv2.line(img, (100,100), (356,356), (255,255,255), 5)##(BB,GG,RR) color code
imgRectangle=cv2.rectangle(img, (100,100), (357,357), (255,255,255), 5)
imgCircle=cv2.circle(img, (229,229), 130, (255,255,255), 5)
imgPutText = cv2.putText(img, 'OPEN CV', (165,400), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,255,255),3)
cv2.imshow('image', img)
cv2.waitKey(0)