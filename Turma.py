class Turma:
    def __init__(self, nome: str, codturma: int):
        self.nome = nome
        self.codturma = codturma
        self.horai = 0
        self.horaf = 0
    
    def sethora(self):
        self.horai = int(input('Horário de ínicio:'))
        self.horaf = int(input('Horário do fim:'))
    def mostraturma(self):
        print(f'A turma {self.nome}, portadora do código {self.codturma}')


    def mostrahora(self):
        print(self.horai, 'h', ' é o horário de ínicio e ', self.horaf, 'h', ' é o horário do fim')

teste = Turma('T.I', 20455)

teste.mostraturma()
teste.sethora()
teste.mostrahora()
