# -*- coding: utf-8 -*-


counters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Вариант 1
odd_items = []
for i in counters:
    if i % 2:
        odd_items.append(i ** 2)

print(odd_items)

# Вариант 2
print(list(map(lambda x: x ** 2, filter(lambda x: x % 2, counters))))

# Вараинт 3
odd_items = [i ** 2 for i in counters if i % 2]
print(odd_items)
