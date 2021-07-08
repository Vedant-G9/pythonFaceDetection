import cv2
import numpy as np

img = cv2.imread('Resources/lena.jpg')

imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) ## converted to black-white
imgBlur=cv2.GaussianBlur(imgGray,(15,15), 0)## converted to Blue img

cv2.imshow('original',img)
cv2.imshow('blk_wht_output',imgGray)
cv2.imshow('Blured_output',imgBlur)
cv2.waitKey(0)