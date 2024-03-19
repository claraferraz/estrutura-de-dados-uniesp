"""Escreva um programa que cria uma lista de nomes e exibe o número total de nomes na lista."""

lista = ["clara", "nisston", "caio", "ana", "maria", "alfredo"]


# len(lista)
def tamanho(lista):
    cont = 0
    for i in lista:
        cont += 1
    print(cont)


tamanho(lista)
