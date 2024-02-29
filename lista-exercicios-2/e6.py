"""Crie uma classe chamada “Produto” com atributos “nome”, “preco” e “quantidade”. 
Implemente um método chamado 
“calcular_total” que retorna o valor total do produto 
(preço * quantidade)."""


class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def calcular_total(self):
        return self.preco * self.quantidade


banana = Produto("banana", 1, 6)
print(banana.calcular_total())
torta = Produto("torta", 25, 3)
print(torta.calcular_total())
