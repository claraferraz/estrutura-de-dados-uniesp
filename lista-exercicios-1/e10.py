""" Crie um programa que simule o jogo "Pedra, Papel e Tesoura" entre o usuário e o computador. 
O programa deve solicitar a escolha do usuário e, em seguida, 
escolher aleatoriamente a escolha do computador e 
determinar o vencedor."""

import random

jogador = input("pedra, papel ou tesoura? ").lower()
computador = random.choice(["pedra", "papel", "tesoura"])
print(f"Você: {jogador}, Computador: {computador}")


def defineVencedor(jogador, computador):
    vitoria = {
        "jogador": "Você ganhou!",
        "computador": "Computador ganhou",
        "empate": "Empate",
    }

    match jogador:
        case "pedra":
            match computador:
                case "pedra":
                    return vitoria["empate"]
                case "papel":
                    return vitoria["computador"]
                case "tesoura":
                    return vitoria["jogador"]
        case "papel":
            match computador:
                case "pedra":
                    return vitoria["jogador"]
                case "papel":
                    return vitoria["empate"]
                case "tesoura":
                    return vitoria["computador"]
        case "tesoura":
            match computador:
                case "pedra":
                    return vitoria["computador"]
                case "papel":
                    return vitoria["jogador"]
                case "tesoura":
                    return vitoria["empate"]
        case _:
            return "erro, jogue novamente"


print(defineVencedor(jogador, computador))
