import cv2
import numpy as np

def empty(v):
    pass
cv2.namedWindow("trackBar") #create window for hue/saturation/value trackbars
cv2.createTrackbar("H min","trackBar",0,179,empty)
cv2.createTrackbar("H max","trackBar",179,179,empty)
cv2.createTrackbar("S min","trackBar",0,255,empty)
cv2.createTrackbar("S max","trackBar",255,255,empty)
cv2.createTrackbar("V min","trackBar",0,255,empty)
cv2.createTrackbar("V max","trackBar",255,255,empty)

cap = cv2.VideoCapture(0) #live_cam_img
while True:
    ret, img = cap.read()
    if ret:
        hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

        # adjusting h_min,s_min,v_min,h_max,s_max,v_max to select color in live_cam_img
        h_min = cv2.getTrackbarPos("H min", "trackBar")
        s_min = cv2.getTrackbarPos("S min", "trackBar")
        v_min = cv2.getTrackbarPos("V min", "trackBar")
        h_max = cv2.getTrackbarPos("H max", "trackBar")
        s_max = cv2.getTrackbarPos("S max", "trackBar")
        v_max = cv2.getTrackbarPos("V max", "trackBar")
        print(f"color's h_min:{h_min},s_min:{s_min},v_min:{v_min},h_max:{h_max},s_max:{s_max},v_max:{v_max}")

        lower = np.array(
            [h_min, s_min, v_min])  # NumPy array or tuple defining the minimum HSV values of the color to detect.
        upper = np.array(
            [h_max, s_max, v_max])  # NumPy array or tuple defining the maximum HSV values of the color to detect.

        mask = cv2.inRange(hsv, lower, upper)  # create the mask
        result = cv2.bitwise_and(img, img, mask=mask)  # place mask onto live_cam_img

        # cv2.imshow("original", img)
        cv2.imshow("mask", mask)
        cv2.imshow("result", result)
    else:
        break
    if cv2.waitKey(1) ==ord("q"):
        break
