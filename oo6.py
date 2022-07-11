class Cliente():
    def __init__(self, nome: str, telefone: str, numero: int, saldo: float, x: float, y: float):
        self.nome = nome
        self.telefone = telefone
        self.numero = numero
        self.saldo =saldo
        self.x = x
        self.y = y

    def mostrardados(self):
        print(f'Nome: {self.nome}, Telefone: {self.telefone}, Número da conta: {self.numero}, Saldo: {self.saldo}, Saque: { self.x}, Depósito: {self.y}')
    
Robson = Cliente('Robson', 21996675019, 209721, 20050, 150, 200)
Robson.mostrardados()
        