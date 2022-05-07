#Morphological transformation 

import cv2
import numpy as np
import pytesseract
from PIL import Image




#using split 
def extractValue(imgOriginal):
    height, width, numChannels = imgOriginal.shape

    imgHSV = np.zeros((height, width, 3), np.uint8)

    imgHSV = cv2.cvtColor(imgOriginal, cv2.COLOR_BGR2HSV)

    imgHue, imgSaturation, imgValue = cv2.split(imgHSV)

    #print(imgOriginal.shape)
    return imgValue

#converting to gray scale 
imgOriginal= cv2.imread('10.png')

imgGrayscale= extractValue(imgOriginal)

structuringElement = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

 
#trying out EROSION
#kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(imgOriginal,structuringElement,iterations = 1)

#trying out dilation
dilation = cv2.dilate(imgOriginal,structuringElement,iterations = 1)
#opening 
opening = cv2.morphologyEx(imgOriginal, cv2.MORPH_OPEN, structuringElement)

#closing
closing = cv2.morphologyEx(imgOriginal, cv2.MORPH_CLOSE, structuringElement)

#hat
imgTopHat = cv2.morphologyEx(imgGrayscale, cv2.MORPH_TOPHAT, structuringElement)
imgBlackHat = cv2.morphologyEx(imgGrayscale, cv2.MORPH_BLACKHAT, structuringElement)

imgGrayscalePlusTopHat = cv2.add(imgGrayscale, imgTopHat)
imgGrayscalePlusTopHatMinusBlackHat = cv2.subtract(imgGrayscalePlusTopHat, imgBlackHat)



#cv2.imshosw('Original Image',imgOriginal)
#cv2.imshow('imgGrayscale',imgGrayscale)
#cv2.imshow('Erosion',erosion)
#cv2.imshow('dilation',dilation)
#cv2.imshow('closing',closing)
#cv2.imshow('opening',opening)
#cv2.imshow('imgTopHat',imgTopHat)
#cv2.imshow('imgBlackHat',imgBlackHat)
#cv2.imshow('imgGrayscalePlusTopHat',imgGrayscalePlusTopHat)
cv2.imshow('imgGrayscalePlusTopHatMinusBlackHat',imgGrayscalePlusTopHatMinusBlackHat)




cv2.destroyAllWindows()




