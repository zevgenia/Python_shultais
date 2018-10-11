# -*- coding: utf-8 -*-
import sys

print("Открыть соединение с БД")

try:
    print("Попытка записать данные")
    raise ValueError
    print("Данные записаны")
except ValueError:
    print("Ошикба: данные неверны")
    sys.exit()
finally:
    print("Закрыть соединение с БД")

print("Продолжение программы")