def get_min_item(items):
    min_item = items[0]
    for item in items[1:]:
        if item < min_item:
            min_item = item
    return min_item

print(get_min_item([23, 4, 7, 4, 12, 6, 8, 41, 20]))
print(get_min_item([5, 4, -12, 5, 6, 7, 8, 1]))
print(get_min_item([54, 14, 12, 15, 60, 7, 8, 19]))
