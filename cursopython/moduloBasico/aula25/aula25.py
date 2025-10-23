"""
Interpolação basica de strings 
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)

Interpolação é um ponco mais antiga e algumas coisas podem nao funcionar atualmente 
"""

nome = 'Igor'
preco = 1000.95897643
# Na interpolação o parenteses só é usado caso queira referenciar mais de uma variavel

variavel = '%s, o preço é R$%.2f' % (nome, preco)
# Senao ficaria assim variavel = '%s, o preço é R$' % nome

print(variavel)
print('O hexadecimal de %d é %04X' % (555,555))
