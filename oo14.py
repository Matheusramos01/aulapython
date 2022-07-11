class Triangulo:
    def __init__(self, A: float, B: float, C: float, p: int):
        self.A = A
        self.B = B
        self.C = C
        self.p = p
    
    def maiorlado(self):
        if(self.A > self.B) and (self.A > self.C):
            print( 'A é o maior lado')
        if(self.B > self.A) and (self.B > self.C):
            print( 'B é o maior lado')
        if(self.C > self.A) and (self.C > self.B):
            print( 'C é o maior lado')
    
    def perimetro(self):
        self.p = self.A + self.B + self.C

mostrar = Triangulo(5, 4, 3, 0)
mostrar.maiorlado()
mostrar.perimetro()
print(vars(mostrar))