# Faça um programa que calcule a média de três números inseridos pelo usuário.

numeros = []

i = 0
while i < 3:
    n = int(input("digite um número: "))
    numeros.append(n)
    i += 1

soma = 0
for i in numeros:
    soma += i

media = soma / 3
print(media)
