# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Author:       Sz
   WeChat:       itlke-sz
-------------------------------------------------
"""
__author__ = 'Sz'

import itchat
from pyecharts.render import make_snapshot

# 使用 snapshot-selenium 渲染图片
from snapshot_selenium import snapshot


# 登录
itchat.auto_login(hotReload=True)
# 获取所有的好友
friends = itchat.get_friends()

# 性别 0 未知  1 男  2 女
sex_titles = ["未知", "男", "女"]
sex_counts = [0, 0, 0]
for friend in friends:
    # print(friend)
    sex = friend["Sex"]
    sex_counts[sex] += 1

print(sex_counts)

from pyecharts.charts import Bar
from pyecharts.options import TitleOpts

bar = Bar()
bar.add_xaxis(sex_titles)
bar.add_yaxis("1组", sex_counts)
bar.set_global_opts(title_opts=TitleOpts(title="撩课-Python-微信数据统计", subtitle="性别统计", title_link="https://www.itlike.com"))
# bar.add_yaxis("2组", [12, 6, 7])

# bar.render()
make_snapshot(snapshot, bar.render(), "sex_count.png")