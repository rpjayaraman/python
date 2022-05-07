import numpy as np
import cv2
import matplotlib.pyplot as plt
from PIL import Image
# GRAY SCALE =0
# IMREAD_COLOR= 1
#IMREAD_UNCHANGED = -1
#place the downloaded image in the same folder 


img= cv2.imread('phone.jpg',cv2.IMREAD_GRAYSCALE)

cv2.imshow('image', img.rotate(45))
cv2.waitKey(0)
cv2.destroyAllWindows()

#plt.imshow(img, cmap='gray', interpolation= 'bicubic')
#plt.plot([],[], 'c', linewidth=5)
#plt.show()
