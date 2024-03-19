"""Escreva um programa que cria uma lista de palavras e exibe a quantidade de palavras que começam
com a letra 'A'."""

lista = ["abacate", "pera", "uva", "maçã", "almondega", "caminhão", "albergue"]
print(lista)


def letraA(lista):
    n = 0
    for i in lista:
        if i[0] == "a":
            n += 1
    print(n)


letraA(lista)
