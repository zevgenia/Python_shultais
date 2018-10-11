sum = 10


def func1():
    #sum = 20
    print('Local1:', sum)


def func2():
    sum = 30
    func1()
    print('Local 2:', sum)

func2()
print("Global:", sum)
