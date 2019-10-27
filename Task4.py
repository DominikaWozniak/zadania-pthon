def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

print(fibo(10))


def fibo_iter():
    numbers = [0, 1]
    zmienna = 0
    for i in range(50):
        zmienna = numbers[-1] + numbers[-2]
        numbers.append(zmienna)
        print(zmienna)

fibo_iter()