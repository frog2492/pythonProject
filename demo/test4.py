# -*- coding: utf-8 -*-
# @Time : 2021/9/24 10:01
# @Author : 袁
# @File : test4.py
# @Software:

def writefile(filename,content):
    f = open(filename,"w")
    for i in content:
        f.write(i)
    f.close()

0
def readfile(filename):
    f = open(filename,"r")
    contents = f.readlines()
    return contents
    f.close

def printfile(filename):
    contents = readfile("gushi.txt")
    for i in contents:
        print(i)
gushi = ["床前明月光，\n疑是地上霜。\n举头望明月，\n低头思故乡。"]
writefile("gushi.txt",gushi)
contents = readfile("gushi.txt")

copy = []
for i in contents:
    copy.append(i)
writefile("copy.txt",copy)

print("---------------------------------")
printfile("gushi.txt")
print("---------------------------------")
printfile("copy.txt")

