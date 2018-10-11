
import sys
s1 = sys.argv[1]
#print(s1)

s2 = set(s1) # преобразовали в неповторяющееся множество
#print(s2)

s3 = list(s2) # преобразовали в список
#print(s3)

s3.sort() # отсортировали список по алфавиту
#print(s3)

line = ''.join(s3) # преобразовать список в строку
print(line)
