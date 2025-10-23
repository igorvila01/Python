# frase = 'O Python é uma linguagem de programação ' \
#         'multiparadigma.' \
#         'Python foi criado por Guido Van Rossum.'

frase = 'aaaooo'

i = 0
qtd_mais_vezes = 0
letra_mais_vezes = ''
while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_atual = frase.count(letra_atual)

    if qtd_mais_vezes < qtd_atual:
        qtd_mais_vezes = qtd_atual
        letra_mais_vezes = letra_atual

    i += 1

print(f'A letra que apareceu mais vezes foi "{letra_mais_vezes}" e ela apareceu {qtd_mais_vezes} vezes')
    
    
