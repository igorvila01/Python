# Introducao as generator functions em python 
# generator = (n for n in range(10))

# def generator(n=0):
#     yield 1 # 1 pausa
#     print('continuando...')
#     yield 2
#     print('Mais uma...')
#     yield 3
#     print('Vou terminar')
#     return 'Acabou'

# gen = generator(n=0)
# for n in gen:
#     print(n)


def generator(n=0, maximo = 10):
    while True:
        yield n
        n += 1

        if n >= maximo:
            return

gen = generator(n=0)
for n in gen:
    print(n)