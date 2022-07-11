class Funcionario:
    def __init__(self, nome: str, cpf: int, salario: float, desconto: float, salarioliquido: float):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario
        self.desconto = desconto
        self.salarioliquido = salarioliquido
        
    def descontar( desconto, salario):
        desconto =  salario * (5/100)

    def calcular(salarioliquido, salario, desconto):
        salarioliquido = salario - desconto    

    def mostrafuncionario(self):
        print(f'Nome: {self.nome}, Cpf: {self.cpf} , Salario:{self.salario}, desconto: {self.desconto}%, Salario Liquido: {self.salarioliquido}')

robson = Funcionario('Robson', 18245176720, 10000, 5.0, 9500)
robson.mostrafuncionario()


