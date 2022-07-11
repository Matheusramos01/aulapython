class Funcionario:
    def __init__(self, nome: str, idade: int, sexo: str, salario: float, ):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.salario = salario
        print(nome, idade, sexo, salario)

    def getSalario(self):
        print('Get Salário', self.salario)

    def setSalario(self, s):
        self.preco = s
        print('Setter Salário', self.salario)
    
    mostrar = property(getSalario, setSalario)
mark = Funcionario('Carlos', 27, 'Masculino', 2500)   
mark.getSalario()
mark.setSalario(2800)
print(vars(mark))