import cv2
import numpy as np

img = cv2.imread("winnie.jpg") #saved pic in the same folder
img = cv2.resize(img,(0,0),fx=0.7,fy=0.7)

hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV) # get the hsv image
def empty(v):
    pass

cv2.namedWindow("trackBar") #create window for hue/saturation/value trackbars
cv2.createTrackbar("H min","trackBar",0,179,empty)
cv2.createTrackbar("H max","trackBar",179,179,empty)
cv2.createTrackbar("S min","trackBar",0,255,empty)
cv2.createTrackbar("S max","trackBar",255,255,empty)
cv2.createTrackbar("V min","trackBar",0,255,empty)
cv2.createTrackbar("V max","trackBar",255,255,empty)

while True:
    # adjusting h_min,s_min,v_min,h_max,s_max,v_max to select color in image
    h_min = cv2.getTrackbarPos("H min", "trackBar")
    s_min = cv2.getTrackbarPos("S min", "trackBar")
    v_min = cv2.getTrackbarPos("V min", "trackBar")
    h_max = cv2.getTrackbarPos("H max", "trackBar")
    s_max = cv2.getTrackbarPos("S max", "trackBar")
    v_max = cv2.getTrackbarPos("V max", "trackBar")
    print(f"color's h_min:{h_min},s_min:{s_min},v_min:{v_min},h_max:{h_max},s_max:{s_max},v_max:{v_max}")

    lower = np.array([h_min,s_min,v_min]) #NumPy array or tuple defining the minimum HSV values of the color to detect.
    upper = np.array([h_max,s_max,v_max]) #NumPy array or tuple defining the maximum HSV values of the color to detect.

    mask = cv2.inRange(hsv,lower,upper) #create the mask
    result = cv2.bitwise_and(img,img,mask=mask) #place mask onto image

    cv2.imshow("original",img)
    cv2.imshow("mask",mask)
    cv2.imshow("result", result)

    cv2.waitKey(1)
