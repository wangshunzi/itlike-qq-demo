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
    sex = friend["Sex"]
    sex_counts[sex] += 1


# print(sex_counts)

# print(list(zip(sex_titles, sex_counts)))

# exit()


from pyecharts.charts import Pie
from pyecharts.options import InitOpts

pie = Pie(init_opts=InitOpts(page_title="撩课-性别统计-饼状图"))

# [("未知", 40), (), ()]
pie.add("性别", list(zip(sex_titles, sex_counts)), radius=["30%", "70%"], rosetype="area")
pie.set_colors(["gray", "orange", "pink"])

pie.render("性别统计-饼状图.html")


