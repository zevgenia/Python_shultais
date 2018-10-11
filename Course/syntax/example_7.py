
age = 20
if age >= 18:
    full_name = "  петров иван иванович  "
    full_name = full_name.title().strip()
    print("Здраствуйте, {1}. Ваш возраст {0} лет. Доступ разрешен".format(age, full_name))
else:
    print("Доступ запрещен")
print("конец")
