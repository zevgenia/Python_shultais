# -*- coding: utf-8 -*-


def sq_all(n):
    return [i ** 2 for i in range(n)]


def sq_iter(n):
    for i in range(n):
        yield i ** 2


print(sq_all(10))
print(sq_iter(10))

sq = sq_iter(5)
#print(sq.__next__())
#print(sq.__next__())
#print(sq.__next__())
#print(next(sq))
#print(next(sq))
#print(next(sq))

for i in sq_iter(5):
    print(i)