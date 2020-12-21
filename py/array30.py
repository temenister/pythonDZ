import random
N = random.randrange(2,11)
print("N = ", N)
a = [random.randrange(1,11) for i in range(N)]
print(a)
kol = 0
for i in range(0,len(a)-1):
    if a[i] > a[i+1]:
        kol += 1
        print("Номер элемента, который больше своего правого соседа:", i)
print("Количество элементов, которые больше своего правого соседа:",kol)