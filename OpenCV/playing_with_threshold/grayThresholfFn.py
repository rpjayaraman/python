from PIL import Image, ImageEnhance, ImageFilter
import cv2
import numpy as np
import pytesseract

#reading and converting imgae to gray 
im= cv2.imread('sixaCrop.jpg',cv2.IMREAD_GRAYSCALE)

#cv2.imshow('Gray', im)
#cv2.imwrite('cardGray.jpg', im)


#applying canny edge detection 
JobEdges= cv2.Canny(im,100,40)
cv2.imshow("Edge Detection", JobEdges)

#save image in jpg format 
#cv2.imwrite('cardCanny.jpg', JobEdges)



#printing text using tesseract 
#print(pytesseract.image_to_string(Image.open('cardGray.jpg')))
#print(pytesseract.image_to_string(Image.open('cardCanny.jpg')))

