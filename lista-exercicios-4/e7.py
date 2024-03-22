"""Crie uma função que aceite um vetor de números inteiros e 
retorne o terceiro maior número. Certifique-se de que sua função funcione 
mesmo se houver números duplicados no vetor."""

# esperado 26
lista = [8, 34, 1, 34, 25, 27, 22, 26, 27, 5, 25, 27, 34, 7]
print(lista)


def ordenaDecrescente(lista):
    if len(lista) <= 1:
        return lista
    ref = lista[0]
    menores = [x for x in lista[1:] if x <= ref]
    maiores = [x for x in lista[1:] if x > ref]
    return ordenaDecrescente(maiores) + [ref] + ordenaDecrescente(menores)


def achaTerMaior(lista):
    listaOrd = ordenaDecrescente(lista)
    print(listaOrd)
    ref = listaOrd[0]
    cont = 1
    for i in range(len(listaOrd)):
        if cont == 3:
            return ref
        elif ref != listaOrd[i]:
            ref = listaOrd[i]
            print(ref)
            cont += 1


print(f"O terceiro maior item da lista é {achaTerMaior(lista)}")
