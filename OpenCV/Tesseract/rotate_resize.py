from  PIL import Image
img= Image.open('phone.jpg')

#rotate 
img.rotate(45).show()
img.save('phone.png')
img.show()
#resize
new= img.resize((400,400))
