
def print_dict(**kwargs):
    for item in kwargs.items():
        print(*item, sep=": ")


fn = "Иван"
ln = "Петров"
p = "Сидорович"
print_dict(last_name=ln, patronymic=p)
