class Funcionario:
    def __init__(self, nome: str, salario: float):
        self.nome = nome
        self.salario = salario

    def aumentasalario(self, salario):
        self.salario = (self.salario) + (self.salario) * (10/100)
    
    def obtersalario(self):
        return self.salario
    
    def mostrarfuncionario(self):
        print(f'Nome: {self.nome}, Salário: {self.salario}')

teste = Funcionario ('Carlos', 25000)
teste.mostrarfuncionario()
teste.aumentasalario(1)
teste.mostrarfuncionario()