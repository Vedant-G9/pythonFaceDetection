import cv2
import numpy as np

img = cv2.imread('Resources/lambo.png')
print(img.shape)
imgResize=cv2.resize(img, (300,200))
print(imgResize.shape)
imgCropped = img[90:400,80:500]
cv2.imshow('orignal', img)
cv2.imshow('Resized_image', imgResize)
cv2.imshow('Cropped_image', imgCropped)
cv2.waitKey(0)