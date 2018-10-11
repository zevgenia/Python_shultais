
import sys
s1 = int(sys.argv[1]) # получаем число
s2 = int(sys.argv[2]) # получаем число
s3 = int(sys.argv[3]) # получаем число
s4 = int(sys.argv[4]) # получаем число
s5 = int(sys.argv[5]) # получаем число
s = [s1, s2, s3, s4, s5] # кортеж чисел
print(str(s))

s.sort(reverse=True)# отсортировали по убыванию

print("сортировка чисел:",s)
print(s[0]) # выводим максмальное
