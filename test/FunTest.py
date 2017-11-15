#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 函数测试
# 只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。
# if 0:
#     print("success")
# if False:
#     print("success")
# if []:
#     print("success")
# if ():
#     print("success")


month = input("Please input your month: ")
m = int(month)
if m <= 12:
    print("success----%d" % m)
else:
    print("Failure----%d" % m)
