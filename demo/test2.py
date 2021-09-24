# -*- coding: utf-8 -*-
# @Time : 2021/9/15 23:23
# @Author : 袁
# @File : test2.py
# @Software:
# 九九乘法表
for x in range(1, 10):
    print("\t")
    for y in range(1, x + 1):
        print("%d*%d=%d" % (x, y, x * y), end="\t")
