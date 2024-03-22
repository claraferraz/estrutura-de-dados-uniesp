"""Escreva uma função em Python para ordenar um vetor de inteiros em ordem crescente usando o
algoritmo de seleção."""

lista = [19, 29, 38, 22, 27, 43, 6, 34, 43, 28]
print(lista)


def ordena(lista):
    n = len(lista)
    for i in range(n):
        min = i
        for j in range(i + 1, n):
            if lista[min] > lista[j]:
                min = j
        aux = lista[i]
        lista[i] = lista[min]
        lista[min] = aux
    print(lista)


ordena(lista)
