"""Escreva um programa que ordene um vetor de inteiros em ordem decrescente e, 
em seguida, conte quantos números pares e quantos números ímpares existem no vetor
ordenado."""

lista = [33, 38, 18, 31, 23, 36, 24, 42, 38, 24]


def ordena(lista):
    if len(lista) <= 1:
        return lista
    ref = lista[0]
    maiores = [x for x in lista[1:] if x >= ref]
    menores = [x for x in lista[1:] if x < ref]
    return ordena(maiores) + [ref] + ordena(menores)


def parImpar(lista):
    listaOrd = ordena(lista)
    pares = []
    impares = []
    for i in listaOrd:
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)

    print(f"lista original: {lista}")
    print(f"lista ordenada: {listaOrd}")
    print(f"lista de pares: {pares}")
    print(f"lista de ímpares: {impares}")


parImpar(lista)
