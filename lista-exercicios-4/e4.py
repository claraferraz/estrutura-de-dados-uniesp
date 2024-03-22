"""Crie uma função que recebe um vetor de números inteiros e retorna o segundo menor número.
Certifique-se de que sua função funcione mesmo se houver números duplicados no vetor."""

# menor 7, segundo menor 11
lista = [12, 20, 28, 7, 11, 45, 11, 21, 7, 7, 46, 49, 28]


def ordena(lista):
    if len(lista) <= 1:
        return lista
    ref = lista[0]
    menores = [x for x in lista[1:] if x <= ref]
    maiores = [x for x in lista[1:] if x > ref]
    return ordena(menores) + [ref] + ordena(maiores)


def achaSegMenor(lista):
    listaOrd = ordena(lista)
    print(listaOrd)
    for i in range(len(listaOrd)):
        if listaOrd[i] != listaOrd[i + 1]:
            return listaOrd[i + 1]


print(f"O segundo menor item da lista é {achaSegMenor(lista)}")
