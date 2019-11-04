import string
def cezar(napis: str, klucz: int):
    alfabet = string.ascii_uppercase
    kod = alfabet[klucz:] + alfabet[:klucz]
    tabela = str.maketrans(alfabet, kod)
    return napis.translate(tabela)


print(cezar('PYTHON', 2))
print(cezar('RAVJQP', -2))

