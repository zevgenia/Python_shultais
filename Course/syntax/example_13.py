# -*- coding: utf-8 -*-

soc = input("Введите название социальной сети: ")
url = ""

if soc == "facebook":
    url = "facebook.com"
elif soc == "vk":
    url = "vk.com"
elif soc == "instagram":
    url = "instagram.com"
elif soc == "ok":
    url = "ok.ru"
elif soc == "twitter":
    url = "twitter.com"
else:
    print("Название не найдено")

if url:
    print("Адрес сети", soc, "=", url)