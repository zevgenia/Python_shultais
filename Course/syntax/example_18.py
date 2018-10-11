
"""j = 1

while True:

    if j == 10:
        break

    if j % 2 == 0:
        print(j)

    j += 1"""


"""
j = 0
while True:
    j += 1

    if j == 10:
        break

    if j % 2 == 0:
        continue

    print(j)
"""

j = 10
while j:
    j -= 1

    if j == 10:
        break

    if j % 2 == 0:
        continue

    print(j)