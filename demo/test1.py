# -*- coding: utf-8 -*-
# @Time : 2021/9/15 21:57
# @Author : 袁
# @File : test1.py
# @Software:
import random

print("规则为 0是石头 1是剪刀 2是布")
y = int(input("出拳:"))
x = random.randint(0, 2)
if y == 2:
    print("人类:布")
elif y == 1:
    print("人类:剪刀")
elif y == 0:
    print("人类:石头")

if x == 2:
    print("电脑:布")
elif x == 1:
    print("电脑:剪刀")
elif x == 0:
    print("电脑:石头")

if y == 2 and x == 0:
    print("人类出布,人类获胜")
elif y == 1 and x == 2:
    print("人类出剪刀,人类获胜")
elif y == 0 and x == 1:
    print("人类出石头,人类获胜")
elif y == x:
    print("比赛平局")
elif y != 1 and y != 2 and y != 0:
    print("你的输入非法")
else:
    if y == 2:
        print("人类出布,电脑获胜")
    elif y == 1:
        print("人类出剪刀,电脑获胜")
    elif y == 0:
        print("人类出石头,电脑获胜")
