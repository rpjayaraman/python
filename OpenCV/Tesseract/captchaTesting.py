from PIL import Image, ImageEnhance, ImageFilter
import pytesseract
#working perfectly for captcha

im= Image.open("captcha.jpg")
im = im.filter(ImageFilter.MedianFilter())
enhancer = ImageEnhance.Contrast(im)
im = enhancer.enhance(2)
im = im.convert('1')
im.save('captchatemp2.jpg')
text = pytesseract.image_to_string(Image.open('captchatemp2.jpg'))
print(text)
