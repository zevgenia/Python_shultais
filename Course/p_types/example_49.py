
cp1251 = open("cp1251.txt", encoding="cp1251")
print(cp1251.read())
cp1251.write("строка")


cp1251 = open("cp1251.txt", "a+", encoding="cp1251")

cp1251.seek(0)
print(cp1251.read())

cp1251.write("\nстрока")
cp1251.seek(0)
print(cp1251.read())