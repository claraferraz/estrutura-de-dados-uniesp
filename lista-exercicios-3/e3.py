"""Escreva um programa que cria uma lista de números inteiros e exibe a soma de todos os números da
lista."""

lista = list(range(3, 22, 3))
print(lista)


# sum(lista)
def somar(lista):
    s = 0
    for i in lista:
        s += i
    print(s)


somar(lista)
