import pytesseract
from PIL import Image, ImageEnhance, ImageFilter

print(pytesseract.image_to_string(Image.open('pytess.png')))
#prints the text from image that we dirtected 
