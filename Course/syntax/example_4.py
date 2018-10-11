
d = 10
l = ("A", "B", "C")
sl = {"en": "one", "ru": "один"}

a = b = c = 10

a *= 5

print(a, b, c)


# Каноническая форма
x = "строка"

# Приваивание кортежей
a, b = 'a', 'b'
print('a:', a)
print('b:', b)

#A, B = ('A', 'B')
#print('A:', A)
#print('B:', B)

# Приваивание списков
d, e = ["d", "e"]
print('d:', d)
print('e:', e)

#d, e, f = ["d", "e"]
#d, e, f = ["d", "e", "f", "g"]
# f = ["a", "b", "c"]

# Приваивание последовательностей
s, t, r, o, k, a = "строка"
a, b, c = ["строка", 45, {1: "one", 2: "two"}]
print('a:', a)
print('b:', b)
print('c:', c)

# Расширенное распаковывание последовательностей
a, *b, c = "A", "B1", "B2", "B3", "C"
print('a:', a)
print('b:', b)
print('c:', c)

# Групповое присваивание одного значения
a = b = c = 0
#c = 0
#b = c
#a = b

# Комбинированное присваивание
a = 10
a += 20
#a = a + 20
print(a)