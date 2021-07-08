import cv2
import numpy as np

img = cv2.imread('Resources/lena.jpg')
imgHor = np.hstack((img, img))
imgVer = np.vstack((img, img))

cv2.imshow('image', img)
cv2.imshow('image_horizatal_stake', imgHor)##horizantal stake
cv2.imshow('image_vertical_stake', imgVer)##vertical Stake

cv2.waitKey(0)