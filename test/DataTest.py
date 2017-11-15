#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print(100 + 200)
print('酷不酷')
print('This is my first', 'Python demo')
print(vars)
print('100+200=', 100 + 200, vars)
print('I\'m \"ok\"')
print('Hello \nleo')
print('\\\t\\')
print(r'\\\t\\')
print('\n')
print('''line1
line2
line3''')
print(not True)

print(True or False)
print(False or False)
print(5 > 6 or 2 < 4)

age = 4
if age >= 5:
    print(age)
elif age <= 3:
    print(age, "--------")
else:
    print(age, "=========")
name = None
print(name)


a = "ABC"
b = a
a = "XYZ"
print('a=',a)
print('b=',b)
A = 1
A=2
print(A)

print(10 / 3)
print(10 // 3)
print(10 % 3)

name = input("Pleast input your name: ")
print('Hello ', name, 'nice to meet your')
