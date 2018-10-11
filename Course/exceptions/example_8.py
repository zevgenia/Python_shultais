# -*- coding: utf-8 -*-

x = None
while True:
    try:
        x = input("Введите число: ")
    except UnicodeDecodeError:
        print("Ошибка, введите число")
        continue
    except Exception:
        print("Ошибка: отчет отправлен разработчикам")
        # Отправляем отчет разработчикам
        exit()

    try:
        x = float(x)
        break
    except ValueError:
        print("Ошибка, введите число")
    except TypeError:
        print("Ошибка, введите число")
    except Exception:
        print("Ошибка: отчет отправлен разработчикам")
        # Отправляем отчет разработчикам
        exit()


try:
    y = 100 / x
except ZeroDivisionError:
    y = "Бесконечность"

print(y)
