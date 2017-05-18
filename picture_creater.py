#-*- coding:utf8 -*-
import sys
import Image
import ImageDraw
import ImageFont
import cv2
# import pyocr
# import pyocr.builders
# from pytesseract import *
import sys
import random
def create_box_file(txt, top):
	with open("hz.font.exp0.box","a") as outf:
		for i in range(len(txt)):
			outf.write( "%s %s %s %s %s\n" %(txt[i], i*6,top-10 ,i*6+6, top))
def create_pic():
	txt = []
	for i in range(0,10):
		txt.append(str(i))
	im = Image.new("RGBA",(200, 1000),(255, 255, 255))
	draw = ImageDraw.Draw(im)
	txt.extend([ ".","/" ])
	for line in range(50):
		draw.text( (0, line*20), "".join(txt) , fill=(0, 0, 0))
		create_box_file(txt, 1000-line*20)
		random.shuffle(txt)
	del draw
	im.save("test", "PNG")


def split_pic():
	img = cv2.imread("test")
	child_img_list = []
	for i in range(25):
		x1 = 0 + i * 6
		x2 = 6 + i * 6
		child_img = img[0:10,x1:x2]
		child_img_list.append(child_img)
		cv2.imwrite(str(i)+".png", child_img)
		child_img = Image.open(str(i)+".png")
		#print image_to_string(child_img)



create_pic()
# import ImageEnhance
split_pic()
# child_img = cv2.imread('test')
# child_img = cv2.resize(child_img,(1800,100),interpolation=cv2.INTER_CUBIC)
# im_gray = cv2.cvtColor(child_img, cv2.COLOR_BGR2GRAY)
# retval, im_at_fixed = cv2.threshold(im_gray, 50, 255, cv2.THRESH_BINARY) 
# cv2.imwrite("test2.png", im_at_fixed)



# child_img = Image.open("test2.png")
# print image_to_string(child_img)
# enhancer = ImageEnhance.Contrast(child_img)
# child_img = enhancer.enhance(4)
# print image_to_string(child_img)


