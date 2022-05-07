from PIL import Image, ImageEnhance, ImageFilter
import cv2
import numpy as np
import pytesseract

#reading and converting imgae to gray 
gray= cv2.imread('noisyNumbers.png',cv2.IMREAD_GRAYSCALE)

gray = cv2.threshold(gray, 150,150,
		cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]


cv2.imshow('Final', gray)
cv2.imwrite('NosiyNoThreshold.jpg', gray)


#applying canny edge detection 
'''
JobEdges= cv2.Canny(im,100,40)
cv2.imshow("Edge Detection", JobEdges)
'''
#save image in jpg format 
#cv2.imwrite('cardCanny.jpg', JobEdges)


#printing text using tesseract 
print(pytesseract.image_to_string(Image.open('NosiyNoThreshold.jpg')))
#print(pytesseract.image_to_string(Image.open('cardCanny.jpg')))

