#!/usr/bin/nnv/python3
# -*- coding: utf-8 -*-
from collections import Iterable, Iterator

print(isinstance('a', Iterable))
print(isinstance(100, Iterable))
print(isinstance([], Iterable))
print(isinstance((), Iterable))
print(isinstance({}, Iterable))
print(isinstance(True, Iterable))
print(isinstance((x for x in range(100) if (x % 2 == 1)), Iterable))
print(isinstance([x for x in range(100) if (x % 2 == 1)], Iterable))

print("-------------is Iterator-----------------------")
print(isinstance('a', Iterator))
print(isinstance(100, Iterator))
print(isinstance([], Iterator))
print(isinstance((), Iterator))
print(isinstance({}, Iterator))
print(isinstance(True, Iterator))
print(isinstance((x for x in range(100) if (x % 2 == 1)), Iterable))
print(isinstance([x for x in range(100) if (x % 2 == 1)], Iterable))


# list tuple dict 虽然都是Iterable 但并不是Iterator
