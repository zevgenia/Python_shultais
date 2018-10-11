# -*- coding: utf-8 -*-


def func(a, b, c):
    print(a, 'and', b, 'and', c)


l = [10, 20, 30]

#func(l)
func(*l)
func(*"xyz")

