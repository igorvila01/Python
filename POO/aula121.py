# Metodos em instancias de classes Python
class Carro:
    def __init__(self, cor, marca, nome):
        self.cor = cor
        self.marca = marca
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} esta acelerando!')
        
fusca = Carro('Branco', 'VW', 'Fusca')
fusca.acelerar()

celta = Carro('Preto', 'GM', 'Celta')
celta.acelerar()