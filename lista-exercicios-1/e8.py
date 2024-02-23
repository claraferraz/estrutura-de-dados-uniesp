# Faça um programa que determine se um número é primo ou não.

n = int(input("Digite um número: "))


def primo(n):
    if n < 2:
        return False
    elif n % 2 == 0:
        return False

    for i in range(2, n // 2):
        if n % i == 0:
            return False
    return True


if primo(n):
    print(f"{n} é primo")
else:
    print(f"{n} não é primo")
