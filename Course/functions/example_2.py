def get_min_item(items):
    if not items:
        return None

    min_item = items[0]
    for item in items[1:]:
        if item < min_item:
            min_item = item
    return min_item

items1 = []
items2 = [5, 4, -12, 5, 6, 7, 8, 1]
items3 = []

print(get_min_item(items1))
print(get_min_item(items2))
print(get_min_item(items3))
