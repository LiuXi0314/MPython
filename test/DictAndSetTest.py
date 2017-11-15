#!/usr/bin/env python3
# -*- coding: utf-8 -*-

nameDict = {'mac': 14, 'ubut': 85, 123: 123}

# dict 类似于java中的map
# 是一种牺牲内存换取时间的方式

if 'mac' in nameDict:
    print(nameDict.get('mac'))
else:
    print(nameDict.items())

# set 无序，会自动过滤list中重复的数据
# set 无序 无重复集合
# listA = [1, 2, 1, 1, 1, 1, 1]
# setA = set(listA)
# print(setA)
#
# setA.add(3)
# setA.add(1)
# print(setA)
tupleA = (1, 2, 3)
tupleB = (1, [2, 3])

tmpDict1 = {tupleA: tupleA}
# tmpDict2 = {tupleB: tupleB}  # error
