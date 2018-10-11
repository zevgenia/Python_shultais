# -*- coding: utf-8 -*-
from math import pi

d = {
    "one": "один",
    2: "two",
    "pi": 3.14
}

print(d)

print(d["one"])
print(d[2])
print(d["pi"])

d["pi"] = pi
print(d)