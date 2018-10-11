# -*- coding: utf-8 -*-


def inc(x):
    return x + 1

counters = [1, 2, 3, 4]

# Вариант 1
# new_counters = []

#for i in counters:
#    new_counters.append(inc(i))

# Вариант 2
#new_counters = list(map(inc, counters))
#print(new_counters)

# Вариант 3
# new_counters = map(inc, counters)
#for item in new_counters:
#    print(item)

# Вариант 4
new_counters = list(map(lambda x: x + 1, counters))
print(new_counters)