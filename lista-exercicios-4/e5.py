"""Implemente uma função que aceite um vetor de números inteiros e 
remova todos os elementos duplicados, retornando o vetor resultante sem duplicatas."""

lista = [42, 38, 43, 38, 7, 29, 9, 29, 8, 20, 44]


def removeRepetidos(lista):
    print(f"lista original: {lista}")
    repetidos = []
    for i in lista:
        if lista.count(i) > 1:
            repetidos.append(i)
            lista.remove(i)
    print(f"elementos repetidos {repetidos}")
    print(f"lista sem duplicatas {lista}")


removeRepetidos(lista)
