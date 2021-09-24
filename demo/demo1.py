# -*- coding: utf-8 -*-
# @Time : 2021/9/15 22:32
# @Author : 袁
# @File : demo1.py
# @Software:
'''
for i in range(5):
    print(i)

for i in range(0, 10, 3):  #从零开始,到10结束,步进值3 (每次+3)
    print(i)
'''
'''
for i in range(-10, -100, -30):
    print(i)

name = "chengdu"
for x in name:
    print(x, end="\t")

a = ["aa", "bb", "cc", "dd"]
for i in range(len(a)):
    print(i, a[i])
'''
'''
i = 0
while i < 5:
    print("当前是第%d次执行循环" % (i + 1))
    print("i=%d" % i)
    i += 1

# 1-100求和
i = 1
sum = 0
while i <= 100:
    sum = sum + i
    i += 1
print("总合为", sum)
'''
'''
count = 0
while count<5:
    print(count,"小于5")
    count+=1
else:
    print(count,"大于或等于5")
'''
'''
i = 0
while i < 10:
    i = i + 1
    print("-" * 30)
    if i == 5:
        break
    print(i)
i = 0
while i < 10:
    i = i + 1
    print("-" * 30)
    if i == 5:
        continue    #结束本次循环
    print(i)
'''
