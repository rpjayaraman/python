import numpy as np
import cv2
import matplotlib.pyplot as plt

# GRAY SCALE =0
# IMREAD_COLOR= 1
#IMREAD_UNCHANGED = -1
#place the downloaded image in the same folder 


img= cv2.imread('phone.jpg',cv2.IMREAD_GRAYSCALE)
#line
#cv2.line(img,(0,0),(50,70),(0,255,0),20)
#rectangle
#cv2.rectangle(img,(0,0),(50,70),(0,0,255),10)
#circle
cv2.circle(img,(100,36),55,(0,0,0),-1)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#plt.imshow(img, cmap='gray', interpolation= 'bicubic')
#plt.plot([],[], 'c', linewidth=5)
#plt.show()
