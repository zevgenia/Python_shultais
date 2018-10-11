
data = {
    "name": "Никита",
    "age": 18,
    "enabled": "рашрешен",
    "disabled": "запрещен"
}

text = "Имя: %(name)s\n" \
       "Возраст: %(age)d\n" \
       "Доступ к сайту: %(enabled)s\n" \
       "Доступ к почте: %(enabled)s\n" \
       "Доступ в офис: %(disabled)s" % data

print(text)
