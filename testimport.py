#!/usr/bin/python
# -*- coding:utf-8 -*-
# import FirstPython
from FirstPython import sum
sum(10,20)
# 打开一个文件
f = open("/Users/KNothing/Desktop/foo.txt", "w")

f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )

# 关闭打开的文件
f.close()