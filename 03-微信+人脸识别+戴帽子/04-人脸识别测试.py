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


def add_hat(image_path, save_path):
    # 1. 加载一个图片
    image = fr.load_image_file(image_path)

    # 2. 人脸识别， 人脸位置
    locations = fr.face_locations(image)

    back_image = Image.open(image_path)
    for location in locations:
        top, right, bottom, left = location
        header = Image.open("images/pig.png")
        face_w = right - left
        face_h = bottom - top
        header.thumbnail((face_w, face_h))
        # (宽， 高)
        header_h = header.size[1]

        back_image.paste(header, box=(left, top - header_h), mask=header)

    back_image.save(save_path)




import itchat

itchat.auto_login(hotReload=True)

myself_username = itchat.get_friends()[0]["UserName"]

header_image = itchat.get_head_img(myself_username)
# print(header_image)

with open("sz_header.png", "wb") as f:
    f.write(header_image)

add_hat("sz_header.png", "sz_hat.png")


