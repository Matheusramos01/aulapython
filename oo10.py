class Carro:
    def __init__(self, modelo: str, consumo: float):
        self.modelo = modelo
        self.consumo = consumo
        self.quantidadecombustivel = 0
    
    def andar(self, distancia):
        litragem = distancia/self.consumo
        self.quantidadecombustivel -= litragem

    def adicionargasolina(self, qtd):
            self.quantidadecombustivel += qtd

    def obtergasolina(self):
        return self.quantidadecombustivel

teste = Carro('Golf', 8)
teste.adicionargasolina(50)
teste.andar(300)
print(vars(teste))
print(teste.obtergasolina())