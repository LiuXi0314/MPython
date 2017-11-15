#!/usr/bin/env python3
# -*- coding: utf-8 -*-
a = 0

# listA = [11, 22, 33, 44, 55, 66]
# for a in listA:
#     b += a
# print(b)
listB = list(range(1000))

for b in listB:
    print(b)
    a += b
print(a)

L = ['Bart', 'Lisa', 'Adam']
for str in L:
    print('Hello %s' % str)
