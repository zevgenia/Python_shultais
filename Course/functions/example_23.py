def get_full_name(first_name, last_name, patronymic=''):
    print(first_name, last_name, patronymic)


fn = "Иван"
ln = "Петров"
p = "Сидорович"

get_full_name(fn, ln, p)
get_full_name(fn, last_name=ln, patronymic=p)
get_full_name(fn, patronymic=p, last_name=ln)