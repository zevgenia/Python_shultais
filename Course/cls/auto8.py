class Auto:

    count = 0
    objects = []

    def __init__(self):
        self.number = ""
        self.power = 0

        Auto.count += 1
        Auto.objects.append(self)

    @staticmethod
    def set_powers(power):
        for obj in Auto.objects:
            obj.power = power


class Bus(Auto):
    pass


auto1 = Auto()
auto2 = Auto()
bus = Bus()

auto1.power = 50
Auto.set_powers(120)
print(auto1.power, auto2.power, bus.power)
