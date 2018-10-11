def get_max(values):
    if not values:
        return None

    max_value = values[0]
    for i in values[1:]:
        if i > max_value:
            max_value = i
    return max_value
