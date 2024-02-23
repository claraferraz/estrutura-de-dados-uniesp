# Escreva um programa que solicite um número ao usuário
# e imprima todos os números pares de 0 até esse número.

n = int(input("Digite um número: "))
pares = []
i = 0
while i <= n:
    if i % 2 == 0:
        pares.append(i)
    i += 1

print(pares)
