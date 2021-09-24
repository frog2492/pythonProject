# -*- coding: utf-8 -*-
# @Time : 2021/9/17 0:21
# @Author : 袁
# @File : test3.py
# @Software:

products = [["iphone", 6680], ["MacPro", 14000], ["xiaomi", 2499], ["Coffee", 31], ["Book", 60], ["Nike", 699]]
print("------商品列表-------")
i = 0
for i ,lis in enumerate (products):
    print("%d" % i, end="\t")
    for li in lis:
        print("%s" % li, end="\t")
    print("\n")
shopping = []
a = 1
num = 0
shoppingname = ""
while(a < len(products)):
    print("请输入产品编号:")
    a = input()
    if a == "q":
        for y in range(0, len(shopping)):
            num = shopping[y][1] + num
            shoppingname += "\n" + shopping[y][0]
        print("你所买的产品有：%s ,\n需要支付价格是：%d" % (shoppingname, num))
        break
    else:
            try:
                a = int(a)
                if (a > 0 and a < 6):
                    shopping.append(products[a])
                    print(shopping)
            except:
                print("输出错误")

'''
products = [["iphone", 6680], ["MacPro", 14000], ["xiaomi", 2499], ["Coffee", 31], ["Book", 60], ["Nike", 699]]
i=0
for number in products:
    print("%d "%(i),end='\t')
    i += 1
    for numbe in number:
        print("%s"%numbe,end='\t')
    print('\n')

shopping = []
a = 1
num = 0
shoppingname = ""
while(a < len(products)):
    print("请输入产品编号")
    a = input()
    if(a == "q"):
        for y in range(0,len(shopping)):
            num = shopping[y][1] + num
            shoppingname +="\n" + shopping[y][0]
        print("你所买的产品有：%s ,\n需要支付价格是：%d" % (shoppingname,num))
        break

    else:
        try:
            a = int(a)
            if (a > 0 and a < 6):
                shopping.append(products[a])
                print(shopping)
        except:
            print("输出错误")
            '''
