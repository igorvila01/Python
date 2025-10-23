"""
Iterando strings com while
"""

nome = 'Igor Vila'  # Iteraveis

contador = 0
resultado = ''

while contador < len(nome):
    resultado += f'*{nome[contador]}'  # Armazenar cada letra na variavel resultado 
    contador += 1
print(resultado)