# Mantendo estado dentro da classe 
class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f'{self.nome} ja esta filmando ...')
            return

        self.filmando = True
        print(f'{self.nome} esta filmando ...')

    def parar_filma(self):
        if not self.filmando:
            print(f'{self.nome} não esta filmando ...')
            return

        self.filmando = False
        print(f'{self.nome} esta parando de filmar ...')
    
    def tirarfoto(self):
        if self.filmando:
            print(f'{self.nome} não pode fotografar enquanto esta filmando!')
            return
        
        print(f'{self.nome} esta fotografando...')
        self.foto = True

    


c1 = Camera('Canon')
c2 = Camera('Sony')

c1.filmar()
c1.filmar()
c1.tirarfoto()
c1.parar_filma()
c1.tirarfoto()
c1.tirarfoto()

# print(c1.filmando)
# print(c2.filmando)
