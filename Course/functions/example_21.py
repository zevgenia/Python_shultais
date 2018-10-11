rus_president_fn = "Владимир"
rus_president_ln = "Путин"
rus_president_p = "Владимирович"
usa_president = ["Барак", "Обама", "Иванович"]
first_rus_president = {"last_name": "Ельцин", "first_name": "Борис"}


def print_full_name(first_name, last_name, patronymic=''):
    print(first_name, patronymic, last_name)


print_full_name(rus_president_fn, rus_president_ln, rus_president_p)
print_full_name(usa_president[0], usa_president[1])
print_full_name(*usa_president)
print_full_name(**first_rus_president)
