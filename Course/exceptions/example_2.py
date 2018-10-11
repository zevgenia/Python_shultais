# -*- coding: utf-8 -*-

x = None
while True:
    x = input("Введите число: ")

    if x.isdigit():
        x = int(x)
        break
    else:
        print("Ошибка, введите число")

y = 100 / x
print(y)
