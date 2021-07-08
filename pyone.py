import cv2
#
# img = cv2.imread('Resources/lena.jpg')
#
# cv2.imshow("Image output",img)
# cv2.waitKey(0)
# print(img)

## Read from webcam
## we have video capture function from the cv2

cap = cv2.VideoCapture(0)

while True:
    success , img = cap.read()
    cv2.imshow("video_ouput",img)
    if cv2.waitKey(1) & 0xFF ==ord('f'): ## to break the loop press 'f'
        break
