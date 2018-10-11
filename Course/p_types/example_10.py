# -*- coding: utf-8 -*-

l = [7, "строка", 2.45]

print(len(l))

print(l[0])

print(l[:-1])



l = [10, "строка", 2.45, "*"]

print(len(l))

print(l[0])

print(l[0:2])

l.append(10)
s2 = l.pop(1)
print(l)
print(s2)

l.remove(10)
print(l)

l.remove(10)
print(l)