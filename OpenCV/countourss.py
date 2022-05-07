import cv2
import numpy as np

cap= cv2.VideoCapture(0)

while 1:
    ret,frame= cap.read()
    hsv= cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_blue= np.array([36,86,0])
    upper_blue= np.array([121,255,255])
    mask= cv2.inRange(hsv, lower_blue, upper_blue)
#draw box around the image 
    _, contours, _= cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(frame, contours, -1, (255,0,255), 2)
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)
    

    key= cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
