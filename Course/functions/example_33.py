# -*- coding: utf-8 -*-


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


print(factorial(120))