#!/usr/bin/env/python3
# -*- coding: utf-8 -*-

# 列表生成器
import os

# 打印上层路径中的文件
print([s for s in os.listdir('../')])
# 打印当前路径中的文件
print([s for s in os.listdir('.')])

print([k + v for k, v in enumerate(range(20, 60))])

print([k + v for k in 'abc' for v in 'def'])

d = {'x': 'A', 'y': 'B', 'z': 'C'}
print([k + '=' + v for k, v in d.items()])

e = ['a', 'a', 'Aa', 'a', 'a', 'a']
print([s.lower() for s in e])

# 练习
ssaL = ['Hello', 'World', 'IBM', 'Apple', 16]
# print([s.lower() for s in ssaL])

print([s.lower() for s in ssaL if isinstance(s, str)])
