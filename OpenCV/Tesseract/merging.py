from PIL import Image


horse= Image.open('unsplash_01.jpg')
phone= Image.open('phone.jpg')
"""
merge
horse_copy= horse.copy()
pos= ((horse_copy.width - phone.width ), (horse_copy.height - phone.height ))
horse_copy.paste(phone, pos)
horse_copy.save('paste_two.jpg')
"""

#flipping
horse_flip= horse.transpose(Image.FLIP_LEFT_RIGHT)
horse_flip.save('horse_flip.jpg')

"""
PIL.Image.FLIP_LEFT_RIGHT,
PIL.Image.FLIP_TOP_BOTTOM,
PIL.Image.ROTATE_90,
PIL.Image.ROTATE_180,
PIL.Image.ROTATE_270
PIL.Image.TRANSPOSE
"""
