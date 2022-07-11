class Disciplina:
    def __init__(self, nome: str, coddisciplina: int):
        self.nome = nome
        self.coddisciplina = coddisciplina
        self.nota = 5
    def disciplinas(self):
        print('Nome da disciplina:', self.nome)
    
    def getnotas(self):
        print('Nota da disciplina b1:', self.nota)
    
    def setnotas(self, n):
        self.nota = n 
        print('Nota da disciplina b2', self.nota)

    def mostradisciplina(self):
        print(f'A turma {self.nome}, código {self.coddisciplina}')

teste =Disciplina('Orientação Objeto', 20455)

teste.mostradisciplina()
teste.getnotas()
teste.setnotas(10)
