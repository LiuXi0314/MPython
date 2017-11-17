#!/usr/bin/env/python3
# -*- coding: utf-8 -*-


# 迭代  iteration


from collections import Iterable

print(isinstance('abc', Iterable))

dict = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
for k in dict:
    print(k)
for v in dict.values():
    print(v)
for k, v in dict.items():
    print(k, ':', v)

for s in "Angelable":
    print(s)

l = ['A', 'B', 'C']
for k, v in enumerate(l):
    print(k, v)
ll = [(1, 'a', True), (2, 'b', True), (3, 'c', False)]

for k, v, vv in ll:
    print(k, v, vv)

# 练习，用迭代找出list中最大值和最小值并输出为一个tuple

testList = [2, 4, 5, 4345, 39, 25, 46, 3224, 85, 342]

min = testList[0]
max = testList[0]
for v in testList:

    if v > max:
        max = v
    elif v < min:
        min = v
print('list 中最大值和最小值分别为：', (max, min))
# 完成练习
