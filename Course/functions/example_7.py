#x = 10

def func1():
    global x
    x = 15
    print(x)

def func2():
    #x = 20
    print(x)

func2()
func1()
print(x)
