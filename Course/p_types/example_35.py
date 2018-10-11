# -*- coding: utf-8 -*-
from copy import deepcopy

d = {1: "one", 2: "two", 3: {"ru": "три", "en": "четыре"}}
d2 = deepcopy(d)

print("D1", d)
print("D2", d2)

d[1] = "один"
d[3]["ru"] = "ТРИ"

print("D1", d)
print("D2", d2)

