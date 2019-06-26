# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Author:       Sz
   WeChat:       itlke-sz
-------------------------------------------------
"""
__author__ = 'Sz'

from pyecharts.charts import Bar

bar = Bar()
bar.add_xaxis(["a", "b", "c"])
bar.add_yaxis("1组", [2, 10, 5])
bar.add_yaxis("2组", [12, 6, 7])

bar.render()