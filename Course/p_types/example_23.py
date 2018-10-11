
f = open("shopping_list2.txt", "w+",encoding="utf-8")
#f = open("shopping_list.txt", "a+", encoding="utf-8")
f.seek(0)
s = f.read()
print("Старый список:\n" + s)
f.write("\nсахар")
f.seek(0)
s = f.read()
print("Новый список:\n" + s)



#f = open("shopping_list2.txt", "w+", encoding="utf-8") # w режим стирания всех данных
# w+ режим подходит для создания нового файла и записи в него данных
f = open("shopping_list.txt", "a+", encoding="utf-8")# режим дозаписи, курсор сдвигается в самый низ
f.seek(0)# смещение курсора в начало
s = f.read()# читает данные из файла начиная с того места где находится курсор и до конца
print(s)
f.write("\nмолоко")# добавляет в строку
f.seek(0)
s = f.read()
print("\n" + s)# вывод нового списка с разделеителем пустой строки
