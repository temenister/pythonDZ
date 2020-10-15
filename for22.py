import math
X=int(input('Введите вещественное число X:'))
N=int(input('Введите целое число N(>0):'))
F = 0
S = 1.0
for i in range(1, N + 1):
        F = X / i
        S += F
        print(i, " : ", F, " : ", S)
print("Result:")
print(S)
print("e:")
print(math.exp(X))