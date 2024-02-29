"""Crie uma classe chamada “Livro” que tenha atributos “titulo” e “autor”. 
Implemente um método
chamado “detalhes” que retorna uma string com as informações do livro."""


class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def detalhes(self):
        print(f"O livro {self.titulo} foi escrito por {self.autor}")


l1 = Livro("Crepúsculo", "Stephenie Meyer")
l1.detalhes()
l2 = Livro("Entendendo Algoritmos", "Aditya Y. Bhargava")
l2.detalhes()
