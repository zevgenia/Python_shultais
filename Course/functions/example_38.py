# -*- coding: utf-8 -*-


def hello(name):
    suffix = "Hello"
    print("%s, %s" % (suffix, name))

x = hello

#print(dir(echo))
print(hello.__name__)
print(x.__name__)
print(hello.__code__.co_varnames)

