# __dict__ e vars para atributos de instancia 

class Pessoa:
    # atributo da classe 
    ano_atual = 2026
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        

    def get_ano_nasc(self):
        return Pessoa.ano_atual - self.idade

dados = {'nome': 'Igor', 'idade': 30}  
p1 = Pessoa(**dados)
# p1.nome = 'Vila'
print(p1.__dict__)
p1.__dict__['nome'] = 'Vila'
print(p1.__dict__)
print(vars(p1))

print(p1.nome)

