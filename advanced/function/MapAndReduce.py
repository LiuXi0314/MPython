#!/usr/bin/env/python3
# -*- coding: utf-8 -*-
from functools import reduce


def fun(x=0):
    return x * x


list_1 = [1, 2, 3, 4, 5]

print(list(map(fun, list_1)))


# 测试

# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
def format_name(name):
    name = name.capitalize()
    print(name)
    return name


list_name = ['adam', 'LISA', 'barT']

m = map(format_name, list_name)
print(list(m))


# reduce

def char2Num(c):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[c]


def xAndy(x, y):
    return x * 10 + y


def reduceTest():
    list = ['1', '2', '3', '4', '5']
    print(reduce(xAndy, map(char2Num, list)))


reduceTest()


def reduceLambda():
    list = ['1', '2', '3', '4', '5']
    print(reduce(lambda x, y: x * 10 + y, map(char2Num, list)))


reduceLambda()
