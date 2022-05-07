#Color trcking
#https://pysource.com/2018/03/01/find-and-draw-contours-opencv-3-4-with-python-3-tutorial-19/
import cv2
import numpy as np
 
cap = cv2.VideoCapture(0)
 
while True:
    _, frame = cap.read()
    #added blurred function to reduce nois
    #removw this to compare with and without noise 
    blurred_frame = cv2.GaussianBlur(frame, (5, 5), 0)
    hsv = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)
 #setting the colour value 
    lower_blue = np.array([38, 86, 0])
    upper_blue = np.array([121, 255, 255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)
 
    _, contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
 
    for contour in contours:
        area = cv2.contourArea(contour)
        print(area)
        if area > 1000:
            cv2.drawContours(frame, contour, -1, (0, 255, 0), 3)
 
 
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)
 
    key = cv2.waitKey(1)
    if key == 27:
        break
 
cap.release()
cv2.destroyAllWindows()

