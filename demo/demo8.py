# -*- coding: utf-8 -*-
# @Time : 2021/9/24 9:10
# @Author : 袁
# @File : demo8.py
# @Software:
#捕获异常
'''try:
    print("-------test---1---")

    f = open('123.txt','r')  #打开一个不存在文件，

    print("-------test-----2--")
except IOError:   #文件未找到，IO异常
    pass     #捕获异常·，执行的代码
    '''

'''
try:
    print(num)
#except IOError: #异常捕获，需一致
except NameError:  
    print("错误产生")
'''

# 获取错误描述
'''
try:
    print("-------test---1---")
   
    f = open('123.txt','r')  #打开一个不存在文件，
    print(num)
    print("-------test-----2--")
except (IOError, NameError) as result:   #
   print(result)
'''
'''
try:
    print("-------test---1---")

    f = open('123.txt', 'r')  # 打开一个不存在文件， 
    print(num)
    print("-------test-----2--")
except Exception as result:  # Exception 可以承接任何异常
    print("产生错误")
    print(result)
    '''

# try ....finally 和嵌套
import time
try:
    f = open("test.txt","r")
    try:
        while True:
            content = f.readline()
            if len(content) == 0 :
                break
            time.sleep(2)
            print(content)
    finally:
        f.close()
        print("文件关闭")

except Exception as result:
    print("发生异常")
    print(result)

