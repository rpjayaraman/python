import cv2 
import numpy as np
import pytesseract
from PIL import Image

img = cv2.imread('job.jpg')
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,100,255,cv2.THRESH_TOZERO_INV)

#HSV
imgHSV= cv2.cvtColor(img, cv2.COLOR_BGR2HSV)



#cv2.imshow('Origianl image',img )
#cv2.imshow('THRESH_BINARY image',thresh1 )
#cv2.imshow('THRESH_BINARY_INV image',thresh2 )
#cv2.imshow('THRESH_TRUNC image',thresh3 )
#cv2.imshow('THRESH_TOZERO image',thresh4 )
#cv2.imshow('THRESH_TOZERO_INV image',thresh5 )
cv2.imshow('HSV', imgHSV)
#cv2.imwrite('HSVwoGray.jpg',imgHSV)

#finding text using tesseract
#print(pytesseract.image_to_string(Image.open('HSVwoGray.jpg')))
