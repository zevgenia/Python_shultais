class Auto:
    def __init__(self):
        self.number = ""
        print("Создание объекта")

auto1 = Auto()
auto2 = Auto()

print("a1:", auto1.number)
auto1.number = "a111aa"
print("a1:", auto1.number)
print("a2:", auto2.number)
auto2.number = "a222aa"
print("a2:", auto2.number)
