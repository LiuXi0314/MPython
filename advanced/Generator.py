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


def pG():
    print(1)
    yield 1
    print(2)
    yield 2
    print(3)


g = pG()
i = 0

while i < 6:
    try:
        next(g)
    except StopIteration as  e:
        print(e.value)
        break
