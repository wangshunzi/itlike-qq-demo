# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Author:       Sz
   WeChat:       itlke-sz
-------------------------------------------------
"""
__author__ = 'Sz'

import face_recognition as fr
from PIL import Image, ImageDraw


# 1. 加载一个图片
image = fr.load_image_file("images/my3.jpg")

# 2. 人脸识别， 人脸位置
locations = fr.face_locations(image)
location = locations[0]
top, right, bottom, left = location

# 3.根据识别的结果， 在人脸的上方添加一个帽子图片

# 3.1 准备好背景图片的画布
back_image = Image.open("images/my3.jpg")
# draw = ImageDraw.Draw(back_image)

# 3.2 在画布上面， 添加另外个帽子图片
header = Image.open("images/pig.png")
face_w = right - left
face_h = bottom - top
header.thumbnail((face_w, face_h))
# (宽， 高)
header_h = header.size[1]

back_image.paste(header, box=(left, top - header_h), mask=header)

back_image.show()







