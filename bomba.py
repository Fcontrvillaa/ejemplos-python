import sys
import time

i = int(sys.argv[1])

while i > 0:
    print(i)
    time.sleep(.33)
    i -= 1

print("booooomm!") 