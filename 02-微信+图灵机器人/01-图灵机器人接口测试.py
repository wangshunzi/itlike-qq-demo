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

def auto_reply(msg):
    # url
    # 请求方式
    # 传递的参数
    url = "http://openapi.tuling123.com/openapi/api/v2"

    data_json = {
        "reqType":0,
        "perception": {
            "inputText": {
                "text": msg
            },
        },
        "userInfo": {
            "apiKey": "bfb59d98d7114998a5118ad7f67c4a59",
            "userId": "itlike"
        }
    }

    # POST
    resp = requests.post(url, json=data_json)

    return resp.json()["results"][0]["values"]["text"]


print(auto_reply("你今天写了几个Bug"))