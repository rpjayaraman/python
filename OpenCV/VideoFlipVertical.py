import numpy as np
import cv2
cap = cv2.VideoCapture(0)
     
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
count=0     
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
#to capture frame after fliping to 90 deg
        frame = cv2.flip(frame,0)
#to capture current frame after it satisfies the condition
        cv2.imwrite("frame%d.jpg" % count, frame)     # save frame as JPEG file
# write the flipped frame
        out.write(frame)
    
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        else:
            break
    
# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
