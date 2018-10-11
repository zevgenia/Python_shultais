# -*- coding: utf-8 -*-


def run(func, arg):
    return func(arg)


l = [1, 2, 3]
for func, arg in [(sum, l), (min, l), (max, [3, 4, 5])]:
    print(run(func, arg))

