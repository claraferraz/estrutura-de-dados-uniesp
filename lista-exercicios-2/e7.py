"""Crie uma classe chamada “Carro” com atributos “marca”, “modelo” e “ano”.
Implemente um método chamado 
“detalhes” que retorna uma string com as informações do carro."""


class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def detalhes(self):
        print(f"{self.modelo} {self.ano} é da {self.marca}")


fusca = Carro("Fusca", 1959, "Volkswagen")
hb20 = Carro("HBO20 Vision 1.0", "Hyundai")
