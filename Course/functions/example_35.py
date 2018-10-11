# -*- coding: utf-8 -*-


def echo(message):
    print(message)


echo("Прямой вызов")

x = echo
x("Косвенный вызов!")