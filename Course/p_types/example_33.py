
from copy import deepcopy

d = {1: "one", 2: "two", 3: {"ru": "три", "en": "четыре"}}
d2 = deepcopy(d)

d[1] = 10
d[3]["ru"] = 333

print(d)
print(d2)
