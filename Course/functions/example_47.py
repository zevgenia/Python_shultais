# -*- coding: utf-8 -*-


print([i ** 2 for i in range(10)])
#print((i ** 2 for i in range(10)))

g = (i ** 2 for i in range(10))
#print(next(g))
#print(next(g))
#print(next(g))
#print(next(g))

print(list(i ** 2 for i in range(10)))
