# -*- coding: utf-8 -*-

x = 42
y = 42

print(x is y)

y = 43
print(x, y, x is y)

import sys
print(sys.getrefcount(1))

