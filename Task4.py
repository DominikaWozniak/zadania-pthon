def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

print(fibo(10))

def fibo_iter(n):
    for i in range(1,n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:



print(fibo_iter(10))