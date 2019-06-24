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



# 1. 登录
itchat.auto_login(hotReload=True)

myself_username = itchat.get_friends()[0]["UserName"]

# 2. 监听别人给我发送文本消息
@itchat.msg_register(itchat.content.TEXT)
def reply_text(msg):
    # 信息是发送给我的微信
    if msg["ToUserName"] == myself_username:
        content = msg["Text"]
        # print("给我发送了一个信息", content)
        reply_msg = Robot.auto_reply(content)
        itchat.send_msg(reply_msg, toUserName=msg["FromUserName"])

# 3. 不断运行
itchat.run()


