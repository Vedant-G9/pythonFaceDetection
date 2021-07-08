import cv2
import numpy as np

img = cv2.imread('Resources/cards.jpg')
width, height = 250,350
pts1 = np.float32([[111,219], [287,188], [154,482], [352,440]])
pts2 = np.float32([[0,0], [width, 0], [0, height], [width, height]])

# cv2.circle(img,(111,219), 10, (0,255,0), 3)
# cv2.circle(img,(287,188), 10, (0,255,0), 3)
# cv2.circle(img,(154,482), 10, (0,255,0), 3)
# cv2.circle(img,(352,440), 10, (0,255,0), 3)

matrix =cv2.getPerspectiveTransform(pts1, pts2)
print(matrix)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))
cv2.imshow('image2', imgOutput)
cv2.imshow('image', img)
cv2.waitKey(0)