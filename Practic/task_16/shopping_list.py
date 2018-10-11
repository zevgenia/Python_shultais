
f = open("shopping_list_1.txt", encoding="utf-8")
s = f.read() # читаем первый список
s = s.split("\n")
s = set(s) # формируем первое множество
#print("список1:\n" + str(s))

f = open("shopping_list_2.txt", encoding="utf-8")
s2 = f.read() # читаем второй список
s2 = s2.split("\n")
s2 = set(s2)# формируем второе множество
#print("список2:\n" + str(s2))

f = open("shopping_list_3.txt", encoding="utf-8")
s3 = f.read() # читаем третий список
s3 = s3.split("\n")
s3 = set(s3)# формируем третье множество
#print("список3:\n" + str(s3))

total = s | s2 | s3 # общее объединенное неповторяющееся множество
#print(total)
t = list(total) # преобразуем в список
t.sort() # сортируем по алфавиту

t = ("\n".join(t)) # склеиваем через перевод строки
#print(t)
f = open("shopping_list.txt", "w+", encoding="utf-8")# создаем новый файл
f.write(t) # записываем туда новый список