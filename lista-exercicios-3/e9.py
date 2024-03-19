"""Escreva um programa que cria duas listas de números inteiros e exibe os números que estão presentes
em ambas as listas."""

li1 = list(range(1, 100, 5))
li2 = list(range(1, 100, 6))
print(li1)
print(li2)


def getIguais(li1, li2):
    iguais = []
    for i in li1:
        if li2.count(i):
            iguais.append(i)

    print(iguais)


getIguais(li1, li2)
