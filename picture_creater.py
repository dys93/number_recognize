#-*- coding:utf8 -*-
import sys
import Image
import ImageDraw
import ImageFont
import cv2
import pyocr
import pyocr.builders
from pytesseract import *
import sys

def create_pic():
	txt = '2017/12/14   10234.56789'
	im = Image.new("RGBA",(200,20),(0,0,0))
	draw = ImageDraw.Draw(im)
	draw.text( (5,5), unicode(txt,'UTF-8'))
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
		print image_to_string(child_img)



create_pic()
import ImageEnhance
#split_pic()
child_img = cv2.imread('test')
child_img = cv2.resize(child_img,(1800,100),interpolation=cv2.INTER_CUBIC)
im_gray = cv2.cvtColor(child_img, cv2.COLOR_BGR2GRAY)
retval, im_at_fixed = cv2.threshold(im_gray, 50, 255, cv2.THRESH_BINARY) 
cv2.imwrite("test2.png", im_at_fixed)



child_img = Image.open("test2.png")
print image_to_string(child_img)
enhancer = ImageEnhance.Contrast(child_img)
child_img = enhancer.enhance(4)
print image_to_string(child_img)


