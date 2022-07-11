class Professor:
    def __init__(self, nome: str,  codprofessor: int, coddisciplina: int):
        self.nome = nome
        self.codprofessor = codprofessor
        self.coddisciplina = coddisciplina
        self.notas = 7
    def cadastro(self):
        print('Professor:', self.nome) 
        print('Código:', self.codprofessor)

    def getnotas(self):
        print('Nota aluno b1:', self.notas)
    
    def setnotas(self, n):
        self.notas = n 
        print('Nota aluno b2', self.notas)

    def mostraprof(self):
        print(f'O professor {self.nome}, portador do código {self.codprofessor} leciona a disciplina {self.coddisciplina}')

teste = Professor('Carlos', 44955, 9467)

teste.cadastro()
teste.mostraprof()
teste.getnotas()
teste.setnotas(10)