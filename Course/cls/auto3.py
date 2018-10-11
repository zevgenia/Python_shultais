class Auto:
    def __init__(self):
        self._number = []

    @property
    def number(self):
        return "".join(self._number)

    @number.setter
    def number(self, number):
        if number.__len__() != 6:
            print("Номер должен состоять из 6 символов")
        else:
            self._number = []
            for i in number:
                self._number.append(i)

auto1 = Auto()
auto1.number = "a111aaa"
print("a1:", auto1.number)
