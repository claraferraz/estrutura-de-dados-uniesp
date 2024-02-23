# Crie um programa que imprima a sequência de Fibonacci
# até um valor inserido pelo usuário.

n = int(input("Digite um número e imprimirei a sequencia de Fribonnacci até ele: "))

fribo = [1, 1]

while (fribo[-2] + fribo[-1]) < n:
    seguinte = fribo[-2] + fribo[-1]
    fribo.append(seguinte)

print(fribo)
