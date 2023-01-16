######################## READ IMAGE ############################
# import cv2
# # LOAD AN IMAGE USING 'IMREAD'
# img = cv2.imread("Resources/lena.png")
# # DISPLAY
# cv2.imshow("Lena Soderberg",img)
# cv2.waitKey(0)

######################### READ VIDEO #############################
# import cv2
# frameWidth = 640
# frameHeight = 480
# cap = cv2.VideoCapture("Resources/test_ video.mp4")
# while True:
#     success, img = cap.read()
#     img = cv2.resize(img, (frameWidth, frameHeight))
#     cv2.imshow("Result", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
######################### READ WEBCAM  ############################
import cv2

print("Packages Installed")

# img = cv2.imread("Resources/lena.png")

# cv2.imshow("Output", img)
# cv2.waitKey(0)


cap = cv2.VideoCapture(0) # default webcam
cap.set(3, 640)  # set the width of the webcam video, 3 is the id of width
cap.set(4, 480)  # set the height of the webcam video, 4 is the id of height
cap.set(10, 100) # set the brightness of the webcam video, 10 is the id of brightness

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    # If you press 'q', the video will close
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
