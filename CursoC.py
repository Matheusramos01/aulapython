class Curso:
    def __init__(self, nome: str,  codcurso: int, codturma: int, coddisciplina: int):
        self.nome = nome
        self.codcurso = codcurso
        self.codturma = codturma 
        self.coddisciplina = coddisciplina
    def montacurso(self):
        print('Curso:', self.nome)
        print('Código do curso:', self.codcurso)
        print('Código da disciplina:', self.coddisciplina)

    def organizar(self):
        print('O curso organizou a turma:', self.codturma)

    def mostracurso(self):
        print(f'O de curso {self.nome}, portador do código {self.codcurso}, da disciplina {self.coddisciplina} para turma {self.codturma}')

teste = Curso('Programação de sistemas', 12665, 9749, 8830)

teste.montacurso()
teste.organizar()
teste.mostracurso()