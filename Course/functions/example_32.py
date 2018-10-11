# -*- coding: utf-8 -*-

a = 2
b = 4


def func(a, b):
    return a * b


def func2():
    global c
    c = a * b


print(func(a, b))
print(func(5, 6))

func2()
print(c)