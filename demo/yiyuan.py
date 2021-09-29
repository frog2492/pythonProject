# -*- coding: utf-8 -*-
# @Time : 2021/9/28 18:25
# @Author : 袁
# @File : yiyuan.py
# @Software:
# 计算一元二次
import cmath
import math

print("方程模版：ax^2+bx+c")

def jisuan(a, b, c):
    if d == 0:
        x1 = x2 = -b / (2 * a)
        print("该方程的根\tx1=x2=%d" % x1)
    else:
        e = math.sqrt(d)
        x1 = (-b + e) / 2 * a
        x2 = (-b - e) / 2 * a
        print("该方程的根x1为%d,x2为%d" % (x1, x2))


while True:
    a = float(input("输入a的值："))
    b = float(input("输入b的值："))
    c = float(input("输入c的值："))
    d = b * b - 4 * a * c
    if a == 0:
        print("非法输入！")
    elif d < 0:
        print("该方程无解")
    else:
        jisuan(a, b, c)
    print("是否继续计算？")
    c = int(input("继续输入1，退出输入0"))
    if c == 1:
        continue
    else:
        break
