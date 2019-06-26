# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Author:       Sz
   WeChat:       itlke-sz
-------------------------------------------------
"""
__author__ = 'Sz'

import itchat
import jieba
import re
from wordcloud import WordCloud

itchat.auto_login(hotReload=True)

friends = itchat.get_friends()

all_words = []
for friend in friends:
    word = friend["Signature"]
    result = jieba.cut(word)
    for w in list(result):
        res = re.match(r"([\u4e00-\u9fa5]+)", w)
        if res:
            all_words.append(res.group(1))

# print(all_words)

# words_count = {}
# for w in all_words:
#     if w not in words_count.keys():
#         words_count[w] = 0
#     words_count[w] += 1
#
# # print(words_count)
#
# sort_words_count = sorted(words_count.items(), key=lambda item: item[1], reverse=True)


from PIL import Image
import numpy as np
from wordcloud import ImageColorGenerator

# 1. 创建一个词云对象

image = Image.open("liao.jpg")
mask = np.array(image)

wc = WordCloud(font_path="title_font.ttf", background_color="white", stopwords={"自己", "世界"}, mask=mask)

# 2. 根据传递的字符串, 生成一个词云图
# 使用空格分割的一个字符串
# a bb cc dd
wc.generate(" ".join(all_words))

wc.recolor(color_func=ImageColorGenerator(mask))

wc.to_file("词云图.png")