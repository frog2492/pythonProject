# -*- coding: utf-8 -*-
# @Time : 2021/9/17 11:45
# @Author : 袁
# @File : demo5.py
# @Software:
'''
tup1=()  #创建空的元组
# tuo2=(50)  #<class 'int'>
#tuo2=(50,)#<class 'tuple'>
tuo2=(50,60,70)
print(type(tup1))
print(type(tuo2))
'''
'''
tup1 = ("abc","def",2000,"苦无",22,44,89,547)
print(tup1[3])
print(tup1[1])
print(tup1[-1])
print(tup1[-2])
print(tup1[1:5])  #进行切片
'''
'''
#增  连接
tup1 = (12,34,56,77)
tup2 = ("abc","cdf")
tup = tup1+tup2
print((tup))
'''

# 删
'''
tup1 = (12,34,56,77)
print(tup1)
del tup1  #删除整个元组变量
print(tup1)  
'''

# 字典定义
'''
info = {"name": "吴彦祖", "age": 18}
# 字典的访问
print(info["name"])
print(info["age"])
# 访问了不存在的健
# print(info["gender"])  #直接访问报错
# print(info.get("gender"))  #使用get方法,没有找到对应的键,默认返回:None
print(info.get("gender", "没有查到"))  # 没有找到时,可以设置默认值
'''
'''
#增
info = {"name": "吴彦祖", "age": 18}
newID = input("请输入学号:")
info["id"] = newID
print(info.get("id"))
'''




#删
'''# [del]
# info = {"name": "吴彦祖", "age": 18}
# print("删除前:%s"%info["name"])
# del info["name"]
# # print("删除后:%s"%info["name"])#删除指定键值对,再次访问报错
# info = {"name": "吴彦祖", "age": 18}
# print("删除前:%s"%info)
# del info["name"]
# print("删除后:%s"%info)
# [clear]
# info = {"name": "吴彦祖", "age": 18}
# print("清空前:%s"%info)
# info.clear()
# print("清空后:%s"%info)'''
#改
'''
info = {"name": "吴彦祖", "age": 18}
info["age"] = 20
print(info["age"])
'''

#查
info = {"id":5,"name": "吴彦祖", "age": 18}
'''
# print(info.keys())  #得到所有的键(列表)
#
# print(info.values())#得到所有的值(列表)
#
# print(info.items())#得到所有的项,每个键值对是一个元组
'''
#遍历所有的值
# 遍历所有的键

'''
for key in info.keys():
    print(key)
    '''

# 遍历所有的值
'''
for value in info.values():
    print(values)'''

#遍历所有的键值对
'''for key,value in info.items():
    print("key=%s,\t values=%s"%(key,value))'''

mylist = ["a","b","c","d"]
# for x in mylist:
#         print(x)
#使用枚举函数,同时拿到列表下标和元素内容
for i,x in enumerate(mylist):
    print(i,x)