import random
n=random.randrange(1,99)
print('Число:',n)
a=0
while n>=1:
        f=n%10
        n//=10
        a=a*10+f
print('Новое число:',a)

