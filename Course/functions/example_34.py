# -*- coding: utf-8 -*-


def factorial(n):
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


print(factorial(0))