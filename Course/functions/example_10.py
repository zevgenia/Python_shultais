# -*- coding: utf-8 -*-

x = 10

def func():
    global x
    x += 5

print(x)
func()
print(x)