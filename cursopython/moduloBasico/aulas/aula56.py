"""
split e join com list e str 
split - divide uma string 
join - une uma string 
"""
frase = '            Olha só que,          coisa interessante          '

# split serve para separar string em uma lista, se o parametro for passado vazio, automaticamente separa por espaços 
lista_frases_cruas = frase.split(', ')
lista_frases = []
# strip corta os espaço do começo e do fim de uma frase, tipo o trim no sql 
# rstrip, corta espaço da direita e lstrip da esquerda 
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

print(lista_frases_cruas)
print(lista_frases)

# join aceita somente string porque numeros nao sao iteraveis 
frases_unidas = ', '.join(lista_frases)
print(frases_unidas)
