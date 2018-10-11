# -*- coding: utf-8 -*-

x = 10

while x:
    x -= 1

    if x % 2:
        continue

    print(x, end=' ')

print()