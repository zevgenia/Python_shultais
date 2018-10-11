G = 9.8


def ek(m, v):
    return (m * (v ** 2)) / 2

if __name__ == "__main__":
    if ek(100, 10) != 5000.:
        print("Ошибка в функции ek")
