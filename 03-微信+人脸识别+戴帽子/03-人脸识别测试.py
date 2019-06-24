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
image = fr.load_image_file("images/double.jpg")

# 2. 人脸识别， 人脸位置
locations = fr.face_locations(image)

back_image = Image.open("images/double.jpg")
for location in locations:
    top, right, bottom, left = location
    header = Image.open("images/pig.png")
    face_w = right - left
    face_h = bottom - top
    header.thumbnail((face_w, face_h))
    # (宽， 高)
    header_h = header.size[1]

    back_image.paste(header, box=(left, top - header_h), mask=header)

back_image.show()







