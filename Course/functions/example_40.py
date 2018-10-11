# -*- coding: utf-8 -*-


counters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_counters = list(filter(lambda x: not x % 2, counters))
print(new_counters)