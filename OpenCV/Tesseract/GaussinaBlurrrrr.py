#Morphological transformation 

import cv2
import numpy as np
import pytesseract
from PIL import Image
from MorphologicalFunctionssss import *

# module level variables
GAUSSIAN_SMOOTH_FILTER_SIZE = (5, 5)
ADAPTIVE_THRESH_BLOCK_SIZE = 19
ADAPTIVE_THRESH_WEIGHT = 9


imgBlurred = cv2.GaussianBlur(imgGrayscalePlusTopHatMinusBlackHat, GAUSSIAN_SMOOTH_FILTER_SIZE, 0)

imgThresh = cv2.adaptiveThreshold(imgBlurred, 255.0, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, ADAPTIVE_THRESH_BLOCK_SIZE, ADAPTIVE_THRESH_WEIGHT)

cv2.imshow('imgBlurred',imgBlurred)
cv2.imshow('imgThresh',imgThresh)

