from random import randint
n=10
print('Число N:',n)
a=[]
for i in range(n):
    a.append(randint(0, n))
a.sort()
print('Набор из целых чисел, упорядоченных по возрастанию:                  ',a)
b=[]
for i in a:
    if i not in b:
        b.append(i)
print('Набор из целых чисел, упорядоченных по возрастанию, но без повторений',b)