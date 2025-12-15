lista = []
for x in range(3):
    for y in range(3):
        lista.append((x,y))

# utilizando um for dentro de outro em list comprehension
lista = [
    (x , y)
    for x in range(3)
    for y in range(3)
]


print(lista)