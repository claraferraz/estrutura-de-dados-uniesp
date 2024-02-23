# Escreva um programa que leia uma lista de nomes e
# retorne uma nova lista com apenas os nomes que
# começam com a letra 'A'.

nomes = ["Andre", "Clara", "João", "Maria", "Amanda", "Ana", "Antonio", "Carlos"]
a = []
for i in nomes:
    if i[0] == "A":
        a.append(i)
print(a)
