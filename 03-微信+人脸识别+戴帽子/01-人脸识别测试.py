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
print(top, right, bottom, left)


# 获取人脸特征
marks = fr.face_landmarks(image)
print(marks)

# exit()
# reb_mark = marks[0]["right_eyebrow"]
reb_mark = marks[0]["right_eye"]
# print(reb_mark)
reb_mark_values = ()
for value in reb_mark:
    reb_mark_values += value
# print(reb_mark_values)

# exit()

# 根据识别到的结果， 绘制一矩形框， 在人脸的位置
my_image = Image.open("images/my3.jpg")

# 根据图片， 创建一个画布， imagedraw
draw = ImageDraw.Draw(my_image)

# 左上右下
draw.rectangle((left, top, right, bottom), outline="red", width=10)

# 画线
draw.line(reb_mark_values, fill="red", width=2)

# 展示图片
# my_image.show()
my_image.save("hecheng_my.jpg")

