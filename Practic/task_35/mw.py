
import sys
line = sys.argv[1]

men = line.count("m")
women = line.count("w")
print("m","(" + str(men) + ")", men * "*")
print("w","(" + str(women) + ")", women * "*")
