from random import randint
n=10
print('Число N:',n)
a=[]
for i in range(n):
    a.append(randint(0, n))
print('Набор из целых чисел:',a)
maxtmp=0
max=0
for i in a:
    if i % 2 == 0:
        maxtmp+=1
    else:
        if maxtmp > max:
            max = maxtmp
        maxtmp = 0
print('Количество четных чисел в наборе, идущих подряд:', max)