# -*- coding: utf-8 -*-

# Ускорение свободного падения
G = 9.8


def ek(m, v):
    return (m * (v ** 2)) / 2


def ep(m, h):
    return m * G * h


if __name__ == "__main__":
    import sys

    #print(sys.argv)

    if "test" in sys.argv and sys.argv[1] == "test":
        if int(ek(100, 10)) != 5000:
            print("Ошибка в функции ek(m, v)")

        if int(ep(100, 10)) != 9800:
            print("Ошибка в функции ep(m, h)")

    if "ek" in sys.argv and sys.argv[1] == "ek":
        print("ek(%s, %s) = %s" % (
            sys.argv[2], sys.argv[3], ek(int(sys.argv[2]), int(sys.argv[3]))
        ))

    if "ep" in sys.argv and sys.argv[1] == "ep":
        print("ep(%s, %s) = %s" % (
            sys.argv[2], sys.argv[3], ep(int(sys.argv[2]), int(sys.argv[3]))
        ))