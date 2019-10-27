rzymskie = {1000: "M", 900: "CM", 500: "D",
            400: "CD", 100: "C", 90: "XC",
            50: "L", 40: "XL", 10: "X",
            9: "IX", 5: "V", 4: "IV", 1: "I"}

def konwertuj():
    liczba = int(input("Podaj liczbę dziesiętną: "))
    for key, value in rzymskie.items():
        if liczba == key:
            print(key, ' = ', value)
    for i in range(0, 1000):
        if i <= 3 and i == liczba:
            print(liczba, ' = ', rzymskie[1] * i)

    else:
        print('liczba nieobsługiwana, prace nad programem w toku')

konwertuj()



