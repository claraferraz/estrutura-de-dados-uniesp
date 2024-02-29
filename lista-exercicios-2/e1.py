"""Crie uma classe chamada “Circulo” que tenha um atributo “raio”.
Implemente um método chamado “calcular_area” que retorna a área do círculo."""


class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return (self.raio**2) * 3.14


c1 = Circulo(5)
print(c1.calcular_area())
c2 = Circulo(10)
print(c2.calcular_area())
