#!/usr/bin/python
# -*- coding:utf-8 -*-
list = [1,2,3,4,5]
print(list)

if(list.__len__() > 5):
    print("more three ")
elif(list.__len__() > 4):
    print("this is elif")
else:
    print("this is else")