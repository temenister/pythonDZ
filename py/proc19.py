import random
import math


def RingS(R1, R2):
    return math.pi * (R1 ** 2 - R2 ** 2)


print('Площади трех колец:\n')

for i in range(0, 3):
    R1 = random.randint(1,10)
    R2 = random.randint(1,R1-1)
    print("R1 = ", R1," R2 = ", R2)
    print("Площадь кольца: ", RingS(R1, R2), '\n')
