"""
Iteravel -> str, range, etc
Iterador -> quem sabe entregar um valor por vez 
next -> me entregue o proximo valor 
iter -> me entregue seu iterador 
"""

# texto = iter('Igor')  # __iter__()

# print(next(texto))

texto = 'Igor'  # iteravel
iterador = iter(texto)   #iterator

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break


