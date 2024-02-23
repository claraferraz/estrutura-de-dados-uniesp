# Faça um programa que leia uma lista de números
# e retorne a média dos números pares.
lista = [40, 98, 57, 4, 38, 5, 70, 3, 1, 547, 31, 42, 10, 85, 76, 0]
soma = 0
n = 1
for i in lista:
    if i % 2 == 0:
        soma += i
        n += 1

media = soma / n
print(media)
