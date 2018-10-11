# -*- coding: utf-8 -*-

x = 10


def func():
    x = 20
    print('Local:', x)

    def func2():
        #global x
        nonlocal x
        #x = 30
        x += 5
        print('Local 2:', x)

    func2()
    print('Local:', x)

func()
print("Global:", x)