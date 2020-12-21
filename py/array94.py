import random
N = random.randrange(3,21)
a = [i for i in range(N)]
print("N = ", N)
print("Массив:",a)
del a[1::2]
print("Массив без нечетных чисел:",a)
