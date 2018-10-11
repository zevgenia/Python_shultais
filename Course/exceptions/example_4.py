# -*- coding: utf-8 -*-

x = None
while True:
    x = input("Введите число: ")

    try:
        x = float(x)
        break
    except ValueError:
        print("Ошибка, введите число")

y = 100 / x
print(y)
