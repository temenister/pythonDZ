import random
import math


def RingS(R1, R2):
    return math.pi * (R1 ** 2 - R2 ** 2)


print('Площади трех колец:\n')

for i in range(0, 3):
    R1R2 = sorted(random.sample(range(1, 10), 2), reverse=True)
    print("R1 = {0}; R2 = {1}".format(R1R2[0], R1R2[1]))
    print("Площадь кольца: ", RingS(R1R2[0], R1R2[1]), '\n')
