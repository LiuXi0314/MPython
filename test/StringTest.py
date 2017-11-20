#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print(ord('a'))
print(ord('A'))
print(chr(69))
x = b'A'
print(x)

print("acs".encode("ascii"))
print("中文".encode("utf-8"))
# print("中文".encode("ascii"))

print(b'acb'.decode('ASCII'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode("UTF-8"))
print(len("你好"))
print(len("你好".encode("utf-8")))

# 占位符测试

print('Hello %s ,Do you have %x RMB?' % ('leo', 0x10002232))

print('%.5f' % 3.123324)
print('%d' % 2)
print('%02d' % 2)
print('小明几年成绩比去年提升了 %04.1f%%' % (85 / 72 - 1))
