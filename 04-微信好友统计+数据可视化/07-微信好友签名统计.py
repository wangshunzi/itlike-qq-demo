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

words_count = {}
for w in all_words:
    if w not in words_count.keys():
        words_count[w] = 0
    words_count[w] += 1

# print(words_count)

sort_words_count = sorted(words_count.items(), key=lambda item: item[1], reverse=True)

# print(sort_words_count)
# exit()

from pyecharts.charts import WordCloud
from pyecharts.globals import SymbolType

wc = WordCloud()

wc.add("itlike", sort_words_count, shape="cardioid")

wc.render("签名统计-词云.html")