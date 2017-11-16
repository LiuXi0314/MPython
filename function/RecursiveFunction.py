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

# 练习
# 请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法。

def move(n, a, b, c):
    if n == 0:
        return 0;
    print(n,'%s = %s' % (b, a))
    print(n,'%s = %s' % (c, b))
    return move(n - 1, a, b, c)

move(10,'A','B','C')