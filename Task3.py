def dzielniki(x, y):
    lista1 = []
    lista2 = []
    for i in range(1, x):
        if x % i == 0:
            lista1.append(i)
    for i in range(1, y):
        if y % i == 0:
            lista2.append(i)
    zbior1 = set(lista1)
    zbior2 = set(lista2)
    print(zbior1)
    print(zbior2)
    print("Część wspólna zbiorów: ", zbior1.intersection(zbior2))


dzielniki(20, 90)