
import sys
import re
l = sys.argv[1]

print(l)
# нужно удалить из строки пробелы и знаки препинания

l = re.sub("[,!.&;:{}?]", " ", l)# заменяем знаки препинания на пробел
l = re.sub("\s{2,}", " ", l)# заменяем множественные пробелы (от 2х) на 1 пробел
l = l.strip()
print(l)
m = l.split(" ")# разбили строку на элементы по пробелам

print(m)
print(str(len(m)))