class Aluno:
    def __init__(self, nome: str, curso: str, temposemdormir: int, tempodeestudo: int):
        self.nome = nome
        self.curso = curso
        self.temposemdormir = temposemdormir
        self.tempodeestudo = tempodeestudo
     
    def estudar(self, temposemdormir):
        self.temposemdormir -= 2
    
    def dormir(self, tempodeestudo):
        self.tempodeestudo += 4
    
    def mostrarAluno(self):
        print(f'Nome: {self.nome}, Curso: {self.curso}, Tempo sem dormir: {self.temposemdormir}, Tempo de estudo: {self.tempodeestudo}')

teste = Aluno('Ana', 'TI', 8, 6)

teste.mostrarAluno()
teste.estudar(10)
teste.dormir(4)        
teste.mostrarAluno()        