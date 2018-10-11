# -*- coding: utf-8 -*-


def func(b):
    b[0] = 1


def func2(b):
    b = b[:]
    b[0] = 2


def func3(b):
    b = b.copy()
    b[0] = 3


l = ['one', 'two', 'three']

func(l[:])
print("l1:", l)

func2(l)
print("l2:", l)

func3(l)
print("l3:", l)