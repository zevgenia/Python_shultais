# -*- coding: utf-8 -*-

x = 10


def func():
    x = 20
    print('Local:', x)

    def func2():
        global y
        nonlocal x
        y = 30
        x += 5

    func2()
    print('Local:', x)

func()
print("Global X:", x)
print("Global Y:", y)