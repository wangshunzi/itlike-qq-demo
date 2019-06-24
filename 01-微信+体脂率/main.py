import itchat
import re

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
        # print(result_notice)

# 先获取我们自己的账号标识

itchat.auto_login(hotReload=True)
myself_username = itchat.get_friends()[0]["UserName"]

@itchat.msg_register(itchat.content.FRIENDS)
def add_friend(msg):
    msg.user.verify()
    msg.user.send('itlike')

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    # return msg.text
    # 谁给我发信息
    if msg["ToUserName"] == myself_username:
        content = msg["Text"]

        result = re.match(r"(.*)[,，](.*)[,，](.*)[,，](.*)[,，](.*)", content)
        # sz,男,18,180,55
        if result:
            # print(result.groups())
            p = Person(*result.groups())
            # print(p.get_body_fat)
            itchat.send_msg(p.get_body_fat, toUserName=msg["FromUserName"])
        else:
            itchat.send_msg("请严格按照数据格式输入：姓名，性别，年龄，身高（cm），体重(kg)",toUserName=msg["FromUserName"])

itchat.run()

