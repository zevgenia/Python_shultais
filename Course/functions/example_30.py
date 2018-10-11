# -*- coding: utf-8 -*-


def func(a, *, c, d=40):
    print('a:', a, 'c:', c, 'd:', d)

func(1, c=3)
func(1, c=6)
func(a=10, c=6, d=20)



