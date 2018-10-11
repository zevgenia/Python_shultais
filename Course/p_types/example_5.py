
animal = "Жыраф шырокий"


print("".upper.__doc__)



animal = "Жираф Широкий"
print(animal)

animal = animal.lower()
print(animal)
print(animal.islower())

animal = animal.upper()
print(animal)
print(animal.isupper())
print(animal.replace("ЖИ", "жы").replace("ШИ","шы").capitalize())

print(dir(""))#распечатал все доступные методы к любой строке

print("".upper.__doc__)#распечатать из встроенной документации как работает метод
print("".capitalize.__doc__)