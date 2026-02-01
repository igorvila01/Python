# Decoradores com paramentros 
def fabrica_de_decoradores(a=None, b=None, c=None):

    def fabrica_de_funcoes(func):
        print('Decorador 1')

        def aninhada(*args, **kwargs):
            print('Parametro decorador', a,b,c)
            print('Aninhada!')
            res = func(*args, **kwargs)
            return res
        return aninhada
    return fabrica_de_funcoes

@fabrica_de_decoradores(1,2,3)
def soma(x,y):
    return x+y

soma_dez_com_cinco = soma(10,5)
fabrica = fabrica_de_decoradores()
multiplica = fabrica(lambda x , y: x * y)

multiplica_dez_com_cinco = multiplica(10,5)

print(soma_dez_com_cinco)
print(multiplica_dez_com_cinco)