import random
import numpy as np

M = random.randrange(1,10)
N = random.randrange(1,10)
print("M = ",M,"; N = ",N)
a = np.random.randint(10, size=(M, N))
print(a)
x=np.prod(a,axis=0)
print("Произведение столбцов:")
print(x)
xmin = min(x)
print("Наименьшее произведение столбца:", xmin)
id=[i for i, y in enumerate(x) if y == xmin]
print("Номер наименьшего столбца:",id)
