# -*- coding: utf-8 -*-

urls = {
    "facebook": "facebook.com",
    "vk.com": "vk.com",
    "instagram": "instagram.com",
    "ok": "ok.ru",
    "twitter": "twitter.com"
}

soc = input("Введите название социальной сети: ")

url = urls.get(soc, "")

if url:
    print("Адрес сети", soc, "=", url)
else:
    print("Название не найдено")