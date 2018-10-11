# -*- coding: utf-8 -*-

l = [1, 2, 3, 4, 5]
res = l[0]
for x in l[1:]:
    res += x

print(res)

# Вариант 2
from functools import reduce

def func(x, y):
    return x + y

print(reduce(func, l))