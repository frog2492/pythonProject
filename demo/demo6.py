# -*- coding: utf-8 -*-
# @Time : 2021/9/17 20:27
# @Author : 袁
# @File : demo6.py
# @Software:

'''
#函数的定义
def printinfo():
    print("----------------")
    print("人生苦短,我用python")
    print("----------------")


#函数的调用
printinfo()
printinfo()'''

'''
#带参数的函数
def addnum(a,b):
    c=a+b
    print(c)

addnum(5,7)'''

'''
# 带返回值的函数

def add2num(a, b):
    return a + b


print(add2num(5, 7))
result = add2num(5, 7)
print(result)
'''

'''
# 返回多个值的函数
def dicid(a, b):
    shang = a / b
    yushu = a % b
    return shang, yushu  #多个返回值用逗号分隔


sh, yu = dicid(5, 2)
print("商%d,余数%d" % (sh, yu))
'''

'''def printx():
    print("-"*30)


printx()
def printnum(a):
    i=0
    while i<a:
        printx()
        i+=1
printnum(5)

def qiuhe(a,b,c):
    d=a+b+c
    return d



def pinjun(a,b,c):
    sum = qiuhe(a,b,c)
    ave = sum/3.0
    return ave
print(pinjun(10,30,27))
'''
'''a=100
def test1():
    a=300     #局部变量
    print("test1-----修改前:a=%d"%a)
    a=200
    print("test1-----修改后:a=%d" % a)
def test2():
    print(a)
test2()
test1()

'''







a=100
def test1():
    global a     #局部变量
    print("test1-----修改前:a=%d"%a)
    a=200
    print("test1-----修改后:a=%d" % a)
def test2():
    print(a)
test2()
test1()










