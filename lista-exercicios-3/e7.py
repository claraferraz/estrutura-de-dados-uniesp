"""Escreva um programa que cria uma lista de números inteiros e exibe os números pares da lista."""

li = list(range(1, 100, 5))
print(li)


def getPares(li):
    pares = []
    for i in li:
        if i % 2 == 0:
            pares.append(i)
    print(pares)


getPares(li)
