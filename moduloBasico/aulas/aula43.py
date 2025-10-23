texto = 'Python'
novo_texto = ''
#  letra é uma variavel que criei na hora 
for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto + '*')