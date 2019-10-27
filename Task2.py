#rekurencja
def silnia(n):
    if n > 1:
        return n * silnia(n - 1)
    elif n in (0, 1):
        return 1


print(silnia(10))

#iteracja

def silnia_iter(n):
    zmienna_pomocnicza = 1
    if n in (0,1):
        return 1
    else:
        for i in range (2, n+1):
            zmienna_pomocnicza = zmienna_pomocnicza * i
        return zmienna_pomocnicza

print(silnia_iter(9))