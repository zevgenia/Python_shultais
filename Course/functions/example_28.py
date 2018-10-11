# -*- coding: utf-8 -*-


def mega_func(a, b=20, c=30, *args, **kwargs):
    print('a:', a)
    print('b:', b)
    print('c:', c)
    print('args:', args)
    print('kwargs:', kwargs)


mega_func(1, 2, 3, 4, 5, e=6, f=7)
mega_func(1, 2, e=5, f=6)
