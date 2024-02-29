"""Crie uma classe chamada “Funcionario” com atributos “nome”, “salario” e “cargo”. 
Implemente um
método chamado “aumentar_salario” que recebe um 
valor percentual de aumento e atualiza o salário
do funcionário."""


class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def aumentar_salario(self, aumento):
        self.salario += (self.salario) * (aumento / 100)
        print(f"Aumento de {aumento}%, salário passa a ser R${self.salario}")


f1 = Funcionario("Clara", 2000, " Desenvolvedora Front-end Jr")
f1.aumentar_salario(10)
