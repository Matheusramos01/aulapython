class Aluno:
    def __init__(self, nome: str,  matricula: int, codturma: int):
        self.nome = nome
        self.matricula = matricula
        self.codturma = codturma
    def cadastro(self):
        print('Nome do aluno:', self.nome)

    def matricular(self):
        print('Matrícula:', self.matricula)
    
    def aula(self):
        print('Acompanhará as aulas da turma:', self.codturma)

    def mostraaluno(self):
        print(f'O aluno {self.nome}, de matrícula {self.matricula} está acompnahará as aulas da turma {self.codturma}')

teste = Aluno('Matheus', 12345, 9879)

teste.cadastro()
teste.matricular()
teste.aula()
teste.mostraaluno()