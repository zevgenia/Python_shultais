
import sys

number = sys.argv[1]

number1 = number[-21:-18]+" "+number[-18:-15]+" "+number[-15:-12]+" "+number[-12:-9]+" "+ \
          number[-9:-6]+" "+ number[-6:-3] +" "+ number[-3:]
print(number1.lstrip())