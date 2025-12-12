import cv2

img = cv2.imread("Lenna.png")
#image downloaded from https://en.wikipedia.org/wiki/Lenna#/media/File:Lenna_(test_image).png
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#below is for face detection
faceCascade = cv2.CascadeClassifier("face_detect.xml")
#find raw data & copy/save .xml file in same folder https://github.com/opencv/opencv/tree/4.x/data/haarcascades

faceRect = faceCascade.detectMultiScale(gray,1.1,3)
for x,y,w,h in faceRect:
    # cv2.rectangle(img,(x,y),(x+w,y+h),[0,0,255],3,lineType=cv2.LINE_8)
    cv2.circle(img,(x+w//2,y+h//2),w//2,[0,0,255],2)

#below is for eye detection
eyeCascade = cv2.CascadeClassifier("eye_detect.xml")
eyeRect = eyeCascade.detectMultiScale(gray,1.05,7)
for x,y,w,h in eyeRect:
    cv2.rectangle(img,(x,y),(x+w,y+h),[255,0,0],2)

#display the circle/rectangle in the original image
cv2.imshow("Lenna_face_and_eye",img)
cv2.waitKey(0)
cv2.destroyAllWindows()