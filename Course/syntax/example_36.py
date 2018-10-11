
items = [4, 7, 2, 3, 5, 13, 4, 8]
# FIXME: Минимальное значение элемента списка
min_item = items[0]
i = 1
# TODO: Улучшить алгоритм
while i < len(items):
    if items[i] < min_item:
        min_item = items[i]
        print(min_item)

    i += 1
