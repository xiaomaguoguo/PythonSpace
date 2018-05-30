#!/usr/bin/python
# -*- coding:utf-8 -*-
seta = {1,2,3,4,5,"KNothing",True}
setb = {2,3,4,5,"KNothing"}
print(seta - setb)  # a和b的差集
print(seta | setb)  # a和b的并集
print(seta & setb)  # a和b的交集
print(seta ^ setb)  # a和b中不同时存在的元素