"""Escreva uma função em Python para ordenar um vetor de inteiros, ele deve receber um parâmetro que
serve como chave para realizar a ordenação crescente ou decrescente."""

lista = [15, 1, 2, 9, 36, 32, 31, 16, 10, 15, 19]


def quick_sort(lista, sentido):
    if len(lista) <= 1:
        return lista

    pivo = lista[0]

    if sentido == "crescente":
        menores = [x for x in lista[1:] if x <= pivo]
        maiores = [x for x in lista[1:] if x > pivo]
        return (
            quick_sort(menores, "crescente") + [pivo] + quick_sort(maiores, "crescente")
        )

    elif sentido == "decrescente":
        maiores = [x for x in lista[1:] if x >= pivo]
        menores = [x for x in lista[1:] if x < pivo]
        return (
            quick_sort(maiores, "decrescente")
            + [pivo]
            + quick_sort(menores, "decrescente")
        )

    else:
        return "escolha crescente ou descrescente"


print(quick_sort(lista, "crescente"))
print(quick_sort(lista, "decrescente"))


# isso:
# menores = [x for x in lista if x < pivot]

# é igual a isso:
#    menores = []
#    for x in lista:
#        if x < pivot:
#            menores.append(x)
