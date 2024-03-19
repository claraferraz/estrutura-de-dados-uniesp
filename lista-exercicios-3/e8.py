"""Escreva um programa que cria uma lista de números inteiros e exibe os números ímimpares da lista."""

li = list(range(1, 100, 5))
print(li)


def getImpares(li):
    impares = []
    for i in li:
        if i % 2 != 0:
            impares.append(i)
    print(impares)


getImpares(li)
