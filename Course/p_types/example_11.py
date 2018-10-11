# -*- coding: utf-8 -*-

l = [7, "строка", 2.45]
print(l)

# Изменение элемента
l[0] = 10
print(l)

# Добавление элемента
l.append(9)
print(l)

# Удаление элемента по индексу
l.pop(1)
print(l)

# Удаление элемента по значению
l.append(10)
print(l)
l.remove(10)
print(l)
l.remove(10)
print(l)

# Вставка элемента по индексу
l.insert(1, 22)
print(l)