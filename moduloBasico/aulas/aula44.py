"""
for + range 
range -> range (start, stop, step)
"""
# range stop, quer dizer que o for vai fazer de zero a 9
numero = range(10)

# range com star e stop, de 5 a 9 
# numero = range(5,10)

# range com start stop de 5 a 9 e de 2 em 2 (se o step for negativo, o start e stop tem que ser negativo )
# numero = range(5,10,2)

for numeros in numero:
    print(numeros)
