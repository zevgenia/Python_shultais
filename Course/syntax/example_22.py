
items = [4, 7, 2, 3, 5, 13, 4, 8]
min_item = items[0]
i = 1

while i < len(items):
    if items[i] < min_item:
        min_item = items[i]

    i += 1

for item in items[1:]:
    if item < min_item:
        min_item = item

print(min_item)
