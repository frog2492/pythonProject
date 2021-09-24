# -*- coding: utf-8 -*-
# @Time : 2021/9/20 20:48
# @Author : 袁
# @File : demo7.py
# @Software:
'''
f = open('test.txt',"w")
f.write("我很忙，牛仔很忙")
f.close()
# read 方法 读取指定的字符，开始时定位在文件头部，每执行一次向后移动指定字符数
f = open("test.txt","r")
content = f.read(5)
print(content)
content = f.read(5)
print(content)
f.close()'''


# f = open("test.txt","r")
# content = f.readlines()
# print(content)
# i = 1
# for temp in content:
#     print("%d:%s"%(i,temp))
#     i+=1
#
# f.close()