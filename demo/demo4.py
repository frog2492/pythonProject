# -*- coding: utf-8 -*-
# @Time : 2021/9/16 22:44
# @Author : 袁
# @File : demo4.py
# @Software:

namelist = ["小张", "小王", "小李"]
'''
testlist = [123,"测试",2.1]
print(testlist[0])
print(testlist[1])
print(type(testlist[0]))
print((type(testlist[1])))
print((type(testlist[2])))
print(namelist[0])
print(namelist[1])
print(namelist[2])'''
'''
for name in namelist:
    print(name)
# print(len(namelist)) #len()可以得到列表的长度
length = len(namelist)
i=0
while i<length:
    print(namelist[i])
    i+=1
'''
# 增   [append]
'''
print("-----增加前,名单列表数据-------")
for name in namelist:
    print(name)
nametemp = input("请输入添加学生姓名:")
namelist.append(nametemp) #在末尾增加一个元素

print("-----增加后,名单列表数据-------")
for name in namelist:
    print(name)
'''
'''
a = [1,2]
b= [3,4]
a.append(b) #讲列表作为一个元素,加入a列表中
print(a)
# 增 [extend]
a.extend(b) #将b列表中的每个元素,逐一追加到a列表中
print(a)
'''
# 增 [insert]
'''
a=[1,2]
a.insert(1,5)  #第一个变量表示下标,第二个表示元素(对象)_
print(a)       #指定下标位置插入元素
'''
'''
# 删 [del] [pop] [remove]
moviename=["加勒比海盗","霸王别姬","蝴蝶效应","指环王","钢铁侠"]
print("-------删除前,电影列表数据-------")
for name in moviename:
    print(name)
# del moviename[2]   #指定位置删除一个元素
# moviename.pop()    #弹出末尾最后一个元素
moviename.remove("钢铁侠") #直接删除指定内容元素 (删除找到的第一个元素)
print("-------删除后,电影列表数据-------")
for name in moviename:
    print(name)
'''
'''
#改
print("-----改前,名单列表数据-------")
for name in namelist:
    print(name)
namelist[1] = "小红"  #修改指定下标元素内容

print("-----改后,名单列表数据-------")
for name in namelist:
    print(name)
'''
'''
# 查 [in , not in]
findname = input("请输入查找学生姓名:")
if findname in namelist:
    print("学员名单有",findname)
else:
 
   print("查无此人")
'''
'''
a = ["a","b","c","a","b"]

print(a.index("a",1,4))  #可以查找指定下标范围元素,并返回找到对应数据的下标
print(a.index("a",1,3))  #范围区间,左闭右开[1,3) ,找不到报错

print(a.count("b")) #统计某个元素出现几次
'''
'''
a = [1, 4, 8, 6, 5]
print(a)
a.reverse()  #将列表所有元素反转
print(a)

a.sort() #升序
print(a)
a.sort(reverse=True)  #降序
print(a)
'''
'''
schoolnames = [[], [], []]  # 有三个元素的空列表,每个元素都是一个空列表
schoolnames = [["北京大学","清华大学"],["南开大学","成都职业技术学院"],["成都工业大学","四川大学","电子科技大学"]]
print(schoolnames)
print(schoolnames[0][1])
'''
import random

offices = [[], [], []]
names = ["A", "B", "C", "D", "E", "F", "G", "H"]
for name in names:
    index = random.randint(0, 2)
    offices[index].append(name)
i = 1
for office in offices:
    print("办公室%d的人数:%d" % (i, len(office)))
    i += 1
    for name in office:
        print("%s" % name, end="\t")
    print("\n")
    print("-" * 30)
