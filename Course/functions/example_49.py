# -*- coding: utf-8 -*-


# Множество
s = set()
for i in range(10):
    s.add(i ** 2)

print({i ** 2 for i in range(10)})
print(s)


# Словарь
d = dict()
for i in range(10):
    d[i] = i ** 2


print({i: i ** 2 for i in range(10)})
print(d)