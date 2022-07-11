class Livro:
    def __init__(self, nome: str, qtdpag: int, autor: str, preco: float):
        self.nome = nome
        self.qtdpag = qtdpag
        self.autor = autor
        self.preco = preco
        print(nome, qtdpag, autor, preco)

    def getPreco(self):
        print('Get preço', self.preco)

    def setPreco(self, a):
        self.preco = a
        print('Setter preço', self.preco)
    
    mostrar = property(getPreco, setPreco)
mark = Livro('Livro M', 320, 'Mt peixoto', 25)   
mark.getPreco()
mark.setPreco(20)
print(vars(mark))
 
    