#!/usr/bin/env python3
# -*- coding: utf-8 -*-

listA = [1,2,3]
print(listA)

listA.clear()
print(listA)

listB = ['a','b','c']
listC = [4]
listA.copy()
print(listA)
print(len(listB))
print(listB[-1])
listB.pop(0)
print(listB[0])
listB.pop(0)
print(listB[0])

# 多维数组
listAA = [1,2,3,[4,5,6,7]]
print(len(listAA))
print(listAA[3][3])

# 元组测试
tupleA = (1, 2, 3, 4)
print(tupleA[1])

tupleB = (0,2)
print(tupleB)

tupleC = (2312,)
print(tupleC)

tupleD = ('1','2','c')


L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0])
print(L[1][1])
print(L[2][2])


