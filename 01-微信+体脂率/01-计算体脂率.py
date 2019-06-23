# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Author:       Sz
   WeChat:       itlke-sz
-------------------------------------------------
"""
__author__ = 'Sz'


# BMI = 体重（kg） / （身高 * 身高）（米）
# 体脂率 = （1.2 * BMI + 0.23 * 年龄 - 5.4 - 10.8*性别（男：1 女：0）） / 100
# 正常成年人的体脂率分别是男性15%~18%和女性25%~28%

# 1. 给输入数据
# name = "sz"
# sex = "男"
# if sex == "男":
#     sex = 1
# else:
#     sex = 0
#
# age = 18
# height = 1.80
# weight = 62

name = input("请输入你的姓名")
sex = input("请输入你的性别")
sex = 1 if sex == "男" else 0
age = int(input("请输入你的年龄"))
height = float(input("请输入你的身高(m)"))
weight = float(input("请输入你的体重(kg)"))


# print(name, sex, age, height, weight)

# exit()

# 2. 计算  处理
BMI = weight / (height * height)
# print(BMI)
body_fat = (1.2 * BMI + 0.23 * age - 5.4 - 10.8 * sex) / 100
print(body_fat)

# 3. 给输出
