import physics


def height(t):

    if t > 10:
        G = 10

    return (physics.G * (t ** 2)) / 2

