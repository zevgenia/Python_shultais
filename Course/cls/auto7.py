class Auto:

    def __init__(self):
        self.number = ""
        self.power = 0

    def get_tax(self):
        rate = 12
        if self.power > 100:
            rate = 25
        return rate * self.power


class Bus(Auto):
    def get_tax(self):
        rate = 15
        return rate * self.power


class InterCityBus(Bus):
    def __init__(self):
        self.city = ""
        super().__init__()

    def get_city(self):
        return self.city

auto = Auto()
auto.power = 101
print("a:", auto.get_tax())

bus = Bus()
bus.power = 300
print("b:", bus.get_tax())

ic_bus = InterCityBus()
ic_bus.power = 200
print("i:", ic_bus.get_tax())
