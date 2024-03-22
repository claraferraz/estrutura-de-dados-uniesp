"""Crie uma função que receba um vetor de números inteiros e retorne a mediana, 
ou seja, o valor do meio quando o vetor é ordenado. 
Certifique-se de que sua função funcione para vetores com um
número ímpar de elementos."""

# len par
lista1 = [34, 50, 41, 50, 37, 13, 20, 39, 21, 3]

# len impar
lista2 = [47, 19, 2, 11, 28, 50, 24, 22, 18, 10, 4]


def ordena(lista):
    if len(lista) <= 1:
        return lista
    ref = lista[0]
    menores = [x for x in lista[1:] if x <= ref]
    maiores = [x for x in lista[1:] if x > ref]
    return ordena(menores) + [ref] + ordena(maiores)


def mediana(lista):
    lo = ordena(lista)
    ind = len(lo) // 2
    m = lo[ind]
    print(f"a mediana da lista ordenada {lo} é {m}")


mediana(lista1)
mediana(lista2)
