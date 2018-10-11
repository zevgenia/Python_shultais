a, b, c = 10, 20, 0


def mult(x, y):
    return x * y


def g_mult():
    global c
    c = a * b
    print(c)

#g_mult()
#print(c)
