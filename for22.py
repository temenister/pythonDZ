X=int(input('Введите вещественное число X:'))
N=int(input('Введите целое число N(>0):'))
a = 1.0+X
B = 1.0
for i in range(1,N+1):
    B *=i
    sum+=a
    print(B)