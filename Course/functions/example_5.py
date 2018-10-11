# -*- coding: utf-8 -*-


def mult(x, y):
    if type(x) not in [int, float] or type(y) not in [int, float]:
        raise TypeError
    return x * y


print(mult(2, 5))
print(mult(3.3, 3))
print(mult("A", 5))