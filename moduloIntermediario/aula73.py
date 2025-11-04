"""
Higher Order Functions 
Funçoes de primeira Classe 
"""
# Não é muito comum colocar print dentro de funçoes 
def saudacao(msg, nome):
    return f'{msg}, {nome}!'

def executa(funcao, *args):
    return funcao(*args)

print(
    executa(saudacao, 'Bom Dia', 'Igor')
)

print(
    executa(saudacao, 'Bom Noite', 'Maria')
)



