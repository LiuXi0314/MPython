#!/usr/bin/env/python3
# -*- coding: utf-8 -*-

# 学习filter 的使用
def isSingle(x):
    return x % 2 == 1


list_new = [1, 2, 34, 5, 65, 6, 7, 7, 8, 443]


def filterTest():
    print(list(filter(isSingle, list_new)))


filterTest()

def filterTest():
    print(list(filter(isSingle, list_new)))

