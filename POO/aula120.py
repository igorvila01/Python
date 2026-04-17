"""
class - Classes são moldes para criar novos objetos 
As classes geram novos objetos (instancias) que podem ter 
seus proprios atributos e metodos.

Os objetos gerados pela classe podem usar seus dados internos para realizar varias açoes.

Por convenção, usamos PascalCase(Quando separa toda palavra utilizando letra maiuscula) 
para nomes de classes.
CriarBaseDeDados
"""

class Pessoa:
    # Def dentro da classe é chamado de metodo 
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
    


p1 = Pessoa('Igor', 'Vila')

print(p1.nome)
print(p1.sobrenome)


p2 = Pessoa('Maria', 'Joana')

print(p2.nome)
print(p2.sobrenome)
