import sys

# Generator expressio, Iterables e Iterators em Python
iterable = ['eu', 'tenho', '__iter__']
iterator = iterable.__iter__()


# Lista salva todos os valores na memoria e o generator somente um valor
# por vez 
lista = [n for n in range(10)]
generator = (n for n in range(10))

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))


# Iterator trabalha com iteravel e é uma classe que trabalha com __iter__
# e next

# Generator é uma função que pausa, quero gerar alguma coisa e pausar 
# toda a execução 