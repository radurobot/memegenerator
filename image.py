import os, random
from extract import jokes
from PIL import Image, ImageDraw, ImageFont

def imgrand():
	path = '/home/radu/projects/pyweb/alldata'
	files = os.listdir(path)
	index = random.randrange(0, len(files))
	#print(files[index])
	return files[index]


def textimg():
	img_number = imgrand()
	path = '/home/radu/projects/pyweb/alldata/'
	img = Image.open(path + img_number)
	img_w, img_h = img.size
	#print(width, heigh)
	background = Image.new('RGB', (500, 500), color = (73, 109, 137))
	bg_w, bg_h = background.size
	offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
	background.paste(img, offset)

	d = ImageDraw.Draw(background)
	#font = ImageFont.truetype("Arial", 25)
	d.text((10,10), jokes(), fill=(255, 255,0))

	background.save('static/save.png')
	#background.show()
	#background.show()
	#img.save('saveimg.png')