
age = 18.5
first_name = "Антон"
d = {
    "name": first_name, "age": age
}
age_str = "Привет. Меня зовут %(name)s. Мне %(age)s лет." % d

print(age_str)
