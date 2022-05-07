#text detection 
import cv2 
import numpy as np
import pytesseract
from PIL import Image

img = cv2.imread('noisyNumbers.png',0)

# Apply dilation and erosion to remove some noise
kernel = np.ones((1, 1), np.uint8)

img = cv2.dilate(img, kernel, iterations=1)
cv2.imshow('dilate', img)

img = cv2.erode(img, kernel, iterations=1)
cv2.imshow('erode', img)


# Write image after removed noise
#cv2.imwrite('removed_noise.jpg', img)
#cv2.imshow('removed_noise.jpg', img)
#  Apply threshold to get image with only black and white
img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
cv2.imshow('adaptive', img)
# Write the image after apply opencv to do some ...
#cv2.imwrite('textOutput.jpg', img)

# Recognize text with tesseract for python
#print(pytesseract.image_to_string(Image.open('textOutput.jpg')))

 # Remove template file
#os.remove(temp)
'''
    print('--- Start recognize text from image ---')
print(get_string("cont.jpg") )

print("------ Done -------")
'''
