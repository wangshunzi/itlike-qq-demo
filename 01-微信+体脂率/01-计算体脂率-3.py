# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Author:       Sz
   WeChat:       itlke-sz
-------------------------------------------------
"""
__author__ = 'Sz'


def get_body_fat(name, sex, age, height, weight):
    try:
        if sex in ("男", "女"):
            sex = 1 if sex == "男" else 0

        # "18"  18
        if isinstance(age, str):
            age = int(age)

        # "180" -> 180
        if isinstance(height, str):
            height = float(height)
            if height > 100:
                # height = height / 100
                height /= 100

        if isinstance(weight, str):
            weight = float(weight)
    except Exception:
        return "请输入正确的数据格式"

    BMI = weight / (height * height)
    body_fat = (1.2 * BMI + 0.23 * age - 5.4 - 10.8 * sex) / 100
    normal_body_fat = ((0.25, 0.28), (0.15, 0.18))
    min_fat_body, max_fat_body = normal_body_fat[sex]
    result = "正常"
    if body_fat < min_fat_body:
        result = "偏瘦"
    elif body_fat > max_fat_body:
        result = "偏胖"
    result_notice = " {} 您好, 您的体脂率是{}, 正常范围是在{} - {}, {}".format(name, body_fat, min_fat_body, max_fat_body, result)
    return result_notice
    # print(result_notice)


name = input("请输入你的姓名")
sex = input("请输入你的性别")
age = input("请输入你的年龄")
height = input("请输入你的身高(m)")
weight = input("请输入你的体重(kg)")

result = get_body_fat(name, sex, age, height, weight)
print(result)