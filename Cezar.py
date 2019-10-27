
def cezar():
    alfabet = ['A']
    zakodowane = []
    literySlowa = []
    key = 2
    pomocnicza = 0
    for i in range(0, 25):
        pomocnicza = ord(alfabet[i]) + 1
        alfabet.append(chr(pomocnicza))

    for i in range(0, 25):
        pomocnicza = ord(alfabet[i]) + key
        zakodowane.append(chr(pomocnicza))

    if ord(zakodowane[24]) > 90:
        zakodowane.remove('[')
        zakodowane.append(chr(65))
        zakodowane.append(chr(66))



    while(True):
        slowoDoKod = input('Podaj slowo do zakodowania, '
                           'wpisuj pojedyncze wielkie litery'
                           'żeby zakonczyc wpisywanie wpisz END: ')
        if slowoDoKod == 'END':
            break
        else:
            literySlowa.append(slowoDoKod)

    print(literySlowa)







cezar()