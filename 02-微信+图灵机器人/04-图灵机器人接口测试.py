# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Author:       Sz
   WeChat:       itlke-sz
-------------------------------------------------
"""
__author__ = 'Sz'

# itchat
# pip install requests
import requests
import itchat
import re

# 图灵机器人自动回复内容
class Robot:
    url = "http://openapi.tuling123.com/openapi/api/v2"
    data_json_temp = """{
        "reqType": 0,
        "perception": {
            "inputText": {
                "text": "%s"
            },
        },
        "userInfo": {
            "apiKey": "bfb59d98d7114998a5118ad7f67c4a59",
            "userId": "itlike"
        }
    }"""
    @classmethod
    def auto_reply(cls, msg):
        data = eval(cls.data_json_temp%msg)
        resp = requests.post(cls.url, json=data)
        return resp.json()["results"][0]["values"]["text"]

# 计算体脂率
class Person:
    def __init__(self, name, sex, age, height, weight):
        try:
            self.name = name
            self.age = 0
            self.height = 0
            self.weight = 0
            self.sex = 0
            if sex in ("男", "女"):
                self.sex = 1 if sex == "男" else 0

            # "18"  18
            if isinstance(age, str):
                self.age = int(age)

            # "180" -> 180
            if isinstance(height, str):
                self.height = float(height)
                if self.height > 100:
                    # height = height / 100
                    self.height /= 100

            if isinstance(weight, str):
                self.weight = float(weight)
        except Exception:
            raise Exception("数据格式有问题")

    @property
    def get_body_fat(self):
        BMI = self.weight / (self.height * self.height)
        body_fat = (1.2 * BMI + 0.23 * self.age - 5.4 - 10.8 * self.sex) / 100
        normal_body_fat = ((0.25, 0.28), (0.15, 0.18))
        min_fat_body, max_fat_body = normal_body_fat[self.sex]
        result = "正常"
        if body_fat < min_fat_body:
            result = "偏瘦"
        elif body_fat > max_fat_body:
            result = "偏胖"
        result_notice = " {} 您好, 您的体脂率是{}, 正常范围是在{} - {}, {}".format(self.name, body_fat, min_fat_body, max_fat_body, result)
        return result_notice

# 微信监听发送给自己， 文本消息
class Wechat:
    """
    {
        r"正则规则1"：函数1，
        r"正则规则2"：函数2，
        r"正则规则3"：函数3，
    }
    """
    def __init__(self, cmd_func_dict):
        # 1. 登录
        itchat.auto_login(hotReload=True)

        # 2. 配置
        self.config(cmd_func_dict)

        # 3. 不断运行
        itchat.run()

    def config(self, cmd_func_dict):
        myself_username = itchat.get_friends()[0]["UserName"]

        # 2. 监听别人给我发送文本消息
        @itchat.msg_register(itchat.content.TEXT)
        def reply_text(msg):
            # 信息是发送给我的微信
            if msg["ToUserName"] == myself_username:
                content = msg["Text"]

                # 关键点
                for cmd, func in cmd_func_dict.items():
                    # print(cmd, func)
                    result = re.match(cmd, content)
                    if result:
                        resp = func(result.groups())
                        itchat.send_msg(resp, toUserName=msg["FromUserName"])


# 实现为王

if __name__ == '__main__':

    # 1. 体脂率计算的规则， 需要执行的函数
    body_fat_re = r"(.*)[,，](.*)[,，](.*)[,，](.*)[,，](.*)"
    def body_fat_caculator(params):
        # print(params)
        p = Person(*params)
        return p.get_body_fat

    # 2. 机器人自动回复的匹配规则， 需要执行的函数
    robot_re = r"lk[,，](.*)"
    def robot_reply(params):
        return Robot.auto_reply(*params)


    Wechat({
        body_fat_re: body_fat_caculator,
        robot_re: robot_reply
    })
