# -*- coding: utf-8 -*-

a = ['a', 'b', 'c', 'd', 'e']
b = ['A', 'B', 'C', 'D', 'E']
c = ('а', 'б', 'в', 'г', 'д')
d = "АБВГД"

for (i, j, k, l) in zip(a, c, b, d):
    s = i + j + k + l
    print(s)