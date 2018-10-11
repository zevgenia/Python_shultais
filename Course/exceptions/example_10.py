# -*- coding: utf-8 -*-
x = None
while True:
    try:
        x = input("Введите число: ")
    #except UnicodeDecodeError:
    #    print("Ошибка, введите число")
    #    continue
    except Exception as e:
        print("Отчет для разработчиков\nОшибка: %s" % e)
        # Отправляем отчет разработчикам
        exit()

    try:
        x = float(x)
        break
    except (ValueError, TypeError):
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
