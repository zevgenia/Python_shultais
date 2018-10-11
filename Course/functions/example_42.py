# -*- coding: utf-8 -*-

def myreduce(function, sequence):
    res = sequence[0]
    for i in sequence[1:]:
        res = function(res, i)
    return res

l = [1, 2, 3, 4, 5]
print(myreduce(lambda x, y: x + y, l))