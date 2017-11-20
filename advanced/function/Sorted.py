#!/usr/bin/env/python3
# -*- coding: utf-8 -*-

# Sorted
list_a = [1, 2, 3, -5, 34, 21, 6]
print(sorted(list_a))

print(list(sorted(list_a,key = abs)))
