# -*- coding: utf-8 -*-
# @Time : 2021/9/15 1:09
# @Author : 袁
# @File : demo.py
# @Software:


print("可以打字了")
a = 10
print("可以显示了", a)
age = 18
print("那年%d" % age)
print("我是%s , 我会%s" % ("学渣", "学习"))
print("aaa", "bbb", "ccc")
print("www", "baidu", "com", sep=".")
print("hello", end="")
print("python", end="\t")
print("world", end="\n")
print("end")
if 11:
    print("True")
else:
    print("False")
print('end')


'''
score = 66
if score >= 90 >= score:
    print("本次考试A")
elif 80 <= score <= 90:
    print("本次考试B")
elif 70 <= score <= 80:
    print("本次考试C")
elif 60 <= score <= 70:
    print("本次考试D")
else:
    print("本次考试E")
'''
import random  # 引入随机库

x = random.randint(0, 2)  # 随机生成0到2三个数 1 2 3
print(x)
