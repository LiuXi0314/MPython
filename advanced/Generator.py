#!/usr/bin/nnv/python3
# -*- coding: utf-8 -*-

# 测试列表生成器


# def fibp(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print(b)
#         a, b = b, a + b
#         n = n + 1
#     return 'done'
#
#
# # fibp(10)
#
#
# def fib(max):
#     a, b = 0, 1
#     while b < max:
#         yield b
#         a, b = b, a + b
#     return 'done'
#
#
# for s in fib(100000):
#     print(s)
#
#
# def pG():
#     print(1)
#     yield 1
#     print(2)
#     yield 2
#     print(3)
#
#
# g = pG()
# i = 0
#
# while i < 6:
#     try:
#         next(g)
#     except StopIteration as  e:
#         print(e.value)
#         break


# 复习练习
# 输出杨辉三角

# [1]
# [1,1]
# [1,2,1]
# [1,3,3,1]
# [1,4,6,4,1]
# [1,5,10,10,5,1]
# [1,6,12,20,12,6,1]

# 利用递归函数去实现的杨辉三角
def creatPasTriangle(input_l: [], limit: 0):
    j = len(input_l)
    new_l = []
    i = 0
    while i < j + 1:
        if i == 0 or i == j:
            new_l.append(1)
            i = i + 1
            continue;
        num = input_l[i - 1] + input_l[i]
        new_l.append(num)
        i = i + 1
    print(new_l)
    if limit == len(new_l):
        print("done")
        return "done"
    return creatPasTriangle(new_l, limit)


# creatPasTriangle([], 10)


# 利用Generator生成器实现杨辉三角的输出
def creatPasTriangleItem(input_l=[]):
    length = len(input_l)
    i = 0
    output_l = []
    while i < length + 1:
        if i == 0 or i == length:
            output_l.append(1)
            i += 1
            continue
        output_l.append(input_l[i - 1] + input_l[i])
        i += 1
    print(output_l)
    return output_l


def pasTriangleGenerator(n):
    i = 0
    origin_l = []
    while i < n:
        origin_l = creatPasTriangleItem(origin_l)
        yield i
        i = i + 1
    return 'done'


def executeGenerator(limit=10):
    g = pasTriangleGenerator(limit)
    while True:
        try:
            next(g)
        except StopIteration as e:
            print(e.value)
            break


executeGenerator()
