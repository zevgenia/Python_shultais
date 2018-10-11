# -*- coding: utf-8 -*-

x = 10


def func():
    global x
    x += 5


def func2():
    print("FUNC 2:", x)


print("INIT:", x)
func()
func2()
print("FINAL:", x)