
def func(arg1, arg2):
    arg1 = 20
    arg2 = arg2[:]
    arg2[0] = 10
    print('arg1', arg1)
    print('arg2', arg2)


ten = 10
l = [1, 2, 3]
func(ten, l)

print("ten:", ten)
print("l:", l)
