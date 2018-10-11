
import sys
s1 = sys.argv[1]
#print(s1)

s2 = list(s1) # преобразовали в список
#print(s2)
s2.sort() # отсортировали по алфавиту список

line = ''.join(s2) # преобразовать список в строку
print(line)
