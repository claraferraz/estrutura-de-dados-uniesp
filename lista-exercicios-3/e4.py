"""Escreva um programa que cria uma lista de números inteiros e exibe a média dos números da lista."""

lista = list(range(1, 30))
print(lista)


# media = sum(lista)/len(lista)
def media(lista):
    n = 0
    soma = 0
    for i in lista:
        soma += i
        n += 1
    return soma / n


print(media(lista))
