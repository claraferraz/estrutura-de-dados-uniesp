"""Crie uma classe chamada “ContaBancaria” que tenha atributos “saldo” e “titular”. 
Implemente métodos “depositar” e “sacar” para manipular o saldo."""


class ContaBancaria:
    def __init__(self, saldo, titular):
        self.saldo = saldo
        self.titular = titular

    def depositar(self, valor):
        self.saldo += valor
        print(f"saldo pós depósito: {self.saldo}")

    def sacar(self, valor):
        self.saldo -= valor
        print(f"saldo pós saque: {self.saldo}")


conta = ContaBancaria(2500, "Maria")
conta.depositar(500)
conta.sacar(100)
