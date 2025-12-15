# list comprehension em python 
# List comprehension é uma forma rapida para criar listas 
# a partir de iteraveis 

# print(list(range(10)))

# lista = []

# for numero in range(10):
#     lista.append(numero)

# print(lista)


# posso fazer um for dentro de uma lista para ser incluido o mesmo valor que foi anteriormente 

lista = [numero for numero in range(10)] 
print(lista)

# posso tambem fazer operaçoes dentro tambem 
lista = [
    numero * 2
    for numero in range(10)
    ] 
print(lista)

