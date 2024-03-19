"""Escreva um programa que cria uma lista de números inteiros e exibe o maior número da lista."""

lista = list(range(10, 60, 5))
print(lista)


# max(lista)
def achaMaior(lista):
    tamanho = len(lista) - 1
    for i in range(0, tamanho):
        if lista[i] > lista[i + 1]:
            print(i)
            m = lista[i]
        else:
            m = lista[i + 1]
    print(m)


achaMaior(lista)
