#cv2.split example 

import cv2
import numpy as np
import pytesseract
from PIL import Image




def extractValue(imgOriginal):
    height, width, numChannels = imgOriginal.shape

    imgHSV = np.zeros((height, width, 3), np.uint8)

    imgHSV = cv2.cvtColor(imgOriginal, cv2.COLOR_BGR2HSV)

    imgHue, imgSaturation, imgValue = cv2.split(imgHSV)

    return imgValue


imgOriginal= cv2.imread('NosiyNoThreshold.jpg')
imgGrayscale= extractValue(imgOriginal)




cv2.imshow('Original Image',imgOriginal)
cv2.imshow('imgGrayscale',imgGrayscale)




