
import numpy as np
import cv2
import time 
cap = cv2.VideoCapture(0)
'''
Changing the frame size by user
ret = cap.set(3,320)
ret = cap.set(4,240)
wid=  cap.get(3)
ht=  cap.get(4)
print(wid)
print(ht)
'''

while(True):
    ret, frame = cap.read()
    cv2.imshow('fram', frame) 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('frame',gray)
    
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
