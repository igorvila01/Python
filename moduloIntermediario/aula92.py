# Yield from
def gen1():
    print('Começou Gen1:')
    yield 1
    yield 2
    yield 3
    print('Acabou Gen1:')

def gen2(gen=None):    
    print('Começou Gen2')
    if gen is not None:
        yield from gen
    yield 4
    yield 5
    yield 6
    print('Acabou Gen2')

def gen3():
    print('Começou Gen3')
    yield 7
    yield 8
    yield 9
    print('Acabou Gen3')



g1 = gen2(gen1())
g2 = gen2(gen3())
g3 = gen2()

for n in g1:
    print(n)
print()

for n in g2:
    print(n)
print()

for n in g3:
    print(n)
print()