# -*- coding: utf-8 -*-


def func(a, *args, c, d=40):
    print('a:', a, 'c:', c, 'd:', d, 'args:', args)

func(1, 2, c=3)
func(1, 2, 3, 4, 5, c=6)
func(a=10, c=6, d=20)



