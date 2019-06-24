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


print(Robot.auto_reply("上行下效"))

