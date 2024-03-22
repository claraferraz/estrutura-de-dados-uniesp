import random


def geraLista(n):
    lista = []
    for i in range(n):
        v = random.randint(1, 50)
        lista.append(v)
    return lista


lista1 = geraLista(11)
print(lista1, len(lista1))
