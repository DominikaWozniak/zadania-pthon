
def cezar():
    literki_lista = ['P', 'Y', 'T', 'H', 'O', 'N']
    zakodowane = []
    odkodowane = []

    for i in range(0,len(literki_lista)):
        x = ord(literki_lista[i])
        if x + 2 > 90 or x < 65:
            x = ord(literki_lista[i])
            zakodowane.append(chr(x - 24))
        else:
            zakodowane.append(chr(x + 2))

    for i in range(0, len(zakodowane)):
        y = ord(zakodowane[i])
        for i in range(0, len(zakodowane)):
            odkodowane.append(chr(y - 2))


    print(zakodowane)
    print(odkodowane)


cezar()


