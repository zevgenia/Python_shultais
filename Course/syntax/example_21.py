# -*- coding: utf-8 -*-

l = [1, 4, 7, 3, 5, 13, 4, 8]

i = 0
ten = False
items = len(l)

while i < items:
    if l[i] >= 10:
        ten = True
        break
    i += 1
#else:
#    print("Все числа меньше 10")

if not ten:
    print("Все числа меньше 10")
