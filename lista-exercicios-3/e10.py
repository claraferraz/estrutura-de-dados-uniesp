"""Escreva um programa que cria uma lista de números inteiros e remove todos os números repetidos,
exibindo a lista resultante."""

lista = [
    1,
    6,
    11,
    16,
    21,
    26,
    31,
    36,
    41,
    46,
    51,
    56,
    61,
    66,
    71,
    76,
    81,
    86,
    91,
    96,
    1,
    7,
    13,
    19,
    25,
    31,
    37,
    43,
    49,
    55,
    61,
    67,
    73,
    79,
    85,
    91,
    97,
]
print(lista)


def removeRepetidos(lista):
    repetidos = []
    for i in lista:
        if lista.count(i) > 1:
            repetidos.append(i)
            lista.remove(i)
    print(repetidos, lista)


removeRepetidos(lista)
