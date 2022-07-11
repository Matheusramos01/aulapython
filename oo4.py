class Pessoa:
    def __init__(self, nome: str, idade: int, altura: float):
        self.nome = nome
        self.idade = idade
        self.altura = altura
    def mostrapessoa(self):
        print(f"nome:{self.nome}, idade{self.idade}, altura:{self.idade}")
pessoa= Pessoa(nome= 'João', idade=25, altura=1.88)
pessoa.mostrapessoa()