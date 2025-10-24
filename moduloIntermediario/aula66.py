"""
Argumentos nomeados e nao nomeados em funçoes Python 
Argumento nomeado tem nome com sinal de igual 
Argumento nao nomeado recebe apenas o argumento (valor)
"""


def soma(x,y, z):
    #definição
    print(f'{x=}  y={y} z={z}', '|' ,'x + y + z = ', x + y + z)

soma(1,2,3)

# A partir do momento que nomeia um argumento, os posteriores devem ser nomeados
# correto deixar todos nomeados ou nao nomeados 
soma(1, y=2, z=5)

