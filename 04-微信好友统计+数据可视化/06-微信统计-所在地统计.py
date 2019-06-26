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
print(sort_addr)

# addr_names = [item[0] for item in sort_addr]
# addr_counts = [item[1] for item in sort_addr]
# print(addr_names, addr_counts)

from pyecharts.charts import Geo
from pyecharts.options import LabelOpts, VisualMapOpts, TitleOpts
from pyecharts.globals import ChartType

geo = Geo()

geo.add_schema(maptype="china")

geo.add("地点统计", sort_addr, type_=ChartType.EFFECT_SCATTER)
geo.set_series_opts(label_opts=LabelOpts(is_show=False))
geo.set_global_opts(
            visualmap_opts=VisualMapOpts(is_piecewise=True,max_=sort_addr[0][1]),
            title_opts=TitleOpts(title="撩课Python统计"),
        )

geo.render("地点统计-geo图.html")
