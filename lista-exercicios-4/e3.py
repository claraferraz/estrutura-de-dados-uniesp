"""Escreva um programa que encontre o elemento máximo em um vetor de inteiros não ordenado sem
usar a função `max()`. Em seguida, encontre o elemento mínimo sem usar a função `min()`."""

lista = [39, 22, 14, 14, 34, 26, 80, 26, 13, 4, 29]


def achaMaior(lista):
    maior = lista[0]
    for i in lista:
        if i > maior:
            maior = i
    print(f"maior: {maior}")


def achaMenor(lista):
    menor = lista[0]
    for i in lista:
        if i < menor:
            menor = i
    print(f"menor: {menor}")


achaMaior(lista)
achaMenor(lista)
