import cv2 
import numpy as np
import pytesseract
from PIL import Image

img = cv2.imread('example.png',0)

# global thresholding
ret1,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

# Otsu's thresholding
ret2,th2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# Otsu's thresholding after Gaussian filtering
blur = cv2.GaussianBlur(img,(5,5),0)
ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow('image',th1)
cv2.imwrite('Otusth1EX.jpg', th1)


#finding text using tesseract
print(pytesseract.image_to_string(Image.open('Otusth1EX.jpg')))

