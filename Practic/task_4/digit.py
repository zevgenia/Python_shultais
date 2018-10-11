
import sys
digit = int(sys.argv[1]) # десятичное число получено

#digit2 = bin(digit).lstrip('-0b') # двоичное число, подавили первые символы признаки системы счисления
#digit8 = oct(digit).lstrip('-0o') # восьмеричное число
#digit16 = hex(digit).lstrip('-0x') # шестнадцатеричное число
#print(digit == bin(digit))
print(digit, bin(digit).lstrip('-0b'), oct(digit).lstrip('-0o'), hex(digit).lstrip('-0x'))