# Atributo de classe 


class Pessoa:
    # atributo da classe 
    ano_atual = 2026
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        

    def get_ano_nasc(self):
        return Pessoa.ano_atual - self.idade
    
p1 = Pessoa('Igor', 30)
p2 = Pessoa('Fran', 29)

print(p1.get_ano_nasc())
print(p2.get_ano_nasc())
