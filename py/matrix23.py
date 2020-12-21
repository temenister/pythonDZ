import random
import numpy as np

M = random.randrange(1,10)
N = random.randrange(1,10)
print("M = ",M,"; N = ",N)
a = np.random.randint(10, size=(M, N))
print(a)
for x in a:
    print("Строка:",x)
    print("Минимальное число в строке:",min(x))