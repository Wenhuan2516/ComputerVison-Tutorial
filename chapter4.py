import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
#print(img)
#img[:]= 255,0,0 img[:] represent the whole image
# img[200:300, 100:300] = 255, 0, 0 this represent part of the image
# print(img.shape) => (512, 512)

# the starting point, the heigth and the width, the color, and how big the line is
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3) # create lines


cv2.rectangle(img,(0,0),(250,350),(0,0,255),2)
cv2.circle(img,(400,50),30,(255,255,0),5)

# the word you want to put, the origin, the font name, the scale, the color, the word size
cv2.putText(img," OPENCV  ",(300,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),3)


cv2.imshow("Image",img)

cv2.waitKey(0)