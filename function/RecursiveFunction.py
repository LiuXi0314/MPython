#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 递归函数练习

def a(i):
    if i <= 0:
        return i
    return a(i - 1)


print(a(20))


def b(n):
    if n == 1:
        return n
    return n * b(n - 1)


print(b(1))
print(b(5))
# 需要好好理解思想


# 任何栈递归的函数都存在栈溢出的问题
# 栈溢出例子
# def c(i):
#     return i*c(i+1)
#
# print(c(1))
