import cv2
import numpy as np

img = cv2.imread("Resources/lambo.png")
print(img.shape)

imgResize = cv2.resize(img,(1000,500)) # 1000 is the width and 500 is the height
print(imgResize.shape)

imgCropped = img[46:119,352:495]  # height first and then width; height from 46 to 119, and width from 352 to 495

cv2.imshow("Image",img)
#cv2.imshow("Image Resize",imgResize)
cv2.imshow("Image Cropped",imgCropped)

cv2.waitKey(0)