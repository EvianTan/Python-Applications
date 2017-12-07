from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

#from PIL import Image, ImasgeDraw, ImageFont

image = Image.open("1sample-in.jpg")

fontType = ImageFont.truetype('Arial.ttf',50)
draw = ImageDraw.Draw(image)
draw.text(xy=(360,10), text='4', fill=(255,0,0), font = fontType)

image.save('1sample-out.jpg')

