import cv2
import numpy as np

img = cv2.imread("img_shape.png")
img = cv2.resize(img,(0,0),fx=0.9,fy=0.9) #re-size the image
img_contour=img.copy()
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gray,20,100)
kernel = np.ones((3,3),np.uint8)
dilate = cv2.dilate(canny,kernel,iterations=1)
contours,hierarchy = cv2.findContours(dilate,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
# print(len(contours))
for contour in contours:
    cv2.drawContours(img_contour, contour, -1, (0, 255, 0), 2)
    area = cv2.contourArea(contour)
    if area>500:
        peri = cv2.arcLength(contour,True)
        vertices = cv2.approxPolyDP(contour, 0.02 * peri, True)
        corners = len(vertices) # this is to tell the types of polygon
        x,y,w,h = cv2.boundingRect(vertices)
        cv2.rectangle(img_contour,(x,y),(x+w,y+h),(255,0,0),2)
        if corners ==3:
            cv2.putText(img_contour,"Triangle",(x,y-10),cv2.FONT_ITALIC,0.5,(0,255,0),2)
        elif corners ==4:
            cv2.putText(img_contour,"Rectangle",(x,y-10),cv2.FONT_ITALIC,0.5,(0,255,0),2)
        else:
            cv2.putText(img_contour, "Others", (x, y-10), cv2.FONT_ITALIC, 0.5, (0, 255, 0), 2)

cv2.imshow("original",img)
cv2.imshow("canny",canny)
cv2.imshow("contoured",img_contour)
cv2.waitKey(0)
