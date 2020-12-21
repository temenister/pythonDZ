def Fib(n):
    F=1
    if n > 2:
        F = Fib(n-1) + Fib(n-2)
    return F

for i in range(1,6):
    x = i
    print(x,":",Fib(x))