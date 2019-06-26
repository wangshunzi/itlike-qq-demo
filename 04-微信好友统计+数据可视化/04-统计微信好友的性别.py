# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Author:       Sz
   WeChat:       itlke-sz
-------------------------------------------------
"""
__author__ = 'Sz'

import itchat
import re
from pyecharts.render import make_snapshot

# 使用 snapshot-selenium 渲染图片
from snapshot_selenium import snapshot


# 登录
itchat.auto_login(hotReload=True)
# 获取所有的好友
friends = itchat.get_friends()

addr_dic = {}
for friend in friends:
    addr = friend["Province"]
    result = re.match(r"([\u4e00-\u9fa5]+)", addr)
    if result:
        provice = result.group(1)
        if provice not in addr_dic.keys():
            addr_dic[provice] = 0
        addr_dic[provice] += 1

# print(addr_dic)

# print(addr_dic.items())
sort_addr = sorted(addr_dic.items(), key=lambda item: item[1], reverse=True)[0:10]
# print(sort_addr)

addr_names = [item[0] for item in sort_addr]
addr_counts = [item[1] for item in sort_addr]
print(addr_names, addr_counts)

from pyecharts.charts import Bar

bar = Bar()
bar.add_xaxis(addr_names)
bar.add_yaxis("1", addr_counts)

bar.render("所在地统计.html")




