from math import sqrt

# Скорость света
C = 299792458


def ek(m, v):
    """
    Кинетическая энергия при скоростях близких к скорости света
    """
    return (m * (C ** 2)) / sqrt(1 - (v ** 2) / (C ** 2)) - (m * (C ** 2))



