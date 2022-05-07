from  PIL import Image
img= Image.open('phone.jpg')



#without damaging aspect ratio
img.thumbnail((400,400))
img.save('thumbnail.jpg')
img.show()


#crop
#box= (150, 200, 300, 400)
c = img.crop((150, 200, 300, 400))
c.save('c1.jpg')
