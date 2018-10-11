# -*- coding: utf-8 -*-

x = 10
y = 20

z = x
x = y
y = z

print(x, y)

x, y = y, x

print(x, y)