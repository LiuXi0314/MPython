#!/usr/bin/nnv/python3
# -*- coding: utf-8 -*-

# 测试列表生成器


def fibp(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'


# fibp(10)


def fib(max):
    a, b = 0, 1
    while b < max:
        yield b
        a, b = b, a + b
    return 'done'


for s in fib(100000):
    print(s)
