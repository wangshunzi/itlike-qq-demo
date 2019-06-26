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
no_mark_sex_counts = [0, 0, 0]
mark_sex_counts = [0, 0, 0]
for friend in friends:
    sex = friend["Sex"]
    if len(friend["RemarkName"]) > 0:
        mark_sex_counts[sex] += 1
    else:
        no_mark_sex_counts[sex] += 1


print(no_mark_sex_counts, mark_sex_counts)

# exit()

from pyecharts.charts import Bar
from pyecharts.options import TitleOpts, InitOpts, ToolboxOpts, AxisOpts

bar = Bar(init_opts=InitOpts(page_title="撩课Python", width="1000px", height="600px"))
bar.add_xaxis(sex_titles)
bar.add_yaxis("有备注", mark_sex_counts, stack="1")
bar.add_yaxis("无备注", no_mark_sex_counts, stack="1")
bar.set_global_opts(title_opts=TitleOpts(title="撩课-Python-微信数据统计", subtitle="性别统计", title_link="https://www.itlike.com"), toolbox_opts=ToolboxOpts(), xaxis_opts=AxisOpts(name="性别"),yaxis_opts=AxisOpts(name="人数", max_=600))
# bar.add_yaxis("2组", [12, 6, 7])

# bar.render()

bar.render("有无备注好友性别统计.html")
# make_snapshot(snapshot, bar.render(), "sex_count.png")