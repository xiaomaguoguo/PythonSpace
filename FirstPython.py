#!/usr/bin/python
# -*- coding: UTF-8 -*-
import keyword

#python保留的关键字
print(keyword.kwlist)

'''
第三注释
第四注释
'''

"""
第五注释
第六注释
"""

print("Hello,KNothing Python World ! ! !")

#缩进表示代码块
if True:
    print("True")
else:
     print("False")

# input("\n\n按下 enter 键后退出。")

import sys
print('================Python import mode==========================');
print ('命令行参数为:')
for i in sys.argv:
    print (i)
print ('\n python 路径为',sys.path)

# help()

a, b, c = 1, 2, "runoob"
print(c)

print ("我叫 %s 今年 %d 岁!" % ('小明', 10))

# a = 10
# def test():
#     nonlocal a
#     global a
#     a = a + 1
    # print(a)
# test()

total = 0 # 这是一个全局变量
# 可写函数说明
def sum( arg1, arg2 ):
    #返回2个参数的和."
    total = arg1 + arg2 # total在这里是局部变量.
    # global total
    # total = 2000
    print ("函数内是局部变量 : ", total)
    return total

#调用sum函数
sum( 10, 20 );
print ("函数外是全局变量 : ", total)

