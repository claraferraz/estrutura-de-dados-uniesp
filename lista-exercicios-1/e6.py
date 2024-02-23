# Escreva um programa que peça um número inteiro positivo ao usuário
# e calcule o fatorial desse número.

n = int(input("Digite um número inteiro positivo: "))
i = 1
fat = 1
while i <= n:
    fat *= i
    i += 1
print(f"{n}! é igual a {fat}")
