import cv2 
import numpy as np
import pytesseract
from PIL import Image

img = cv2.imread('temp2.jpg',0)


th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,15,15)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)

#cv2.imshow('Origianl image',img )

cv2.imshow('th mean',th2 )
#cv2.imshow('th Gaussian',th3 )

cv2.imwrite('crop.jpg',th2)

#finding text using tesseract
print(pytesseract.image_to_string(Image.open('crop.jpg')))

