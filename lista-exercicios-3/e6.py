"""Escreva um programa que cria uma lista de strings e exibe a mais longa palavra da lista."""

lista = [
    "abacate",
    "pera",
    "uva",
    "maçã",
    "almondega",
    "caminhão",
    "albergue",
    "paralelepípedo",
]
print(lista)


def palavraMaior(lista):
    n = len(lista)
    maior = lista[0]

    for i in range(0, n):
        if len(maior) < len(lista[i]):
            maior = lista[i]
    print(maior)


palavraMaior(lista)
