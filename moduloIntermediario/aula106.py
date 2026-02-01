# Ordem dos decoradores 
def parametro_decorador(nome):
    def decorador(func):
        print('Decorador: ',nome)

        def sua_nova_funcao(*args, **kwargs):
            resultado = func(*args, **kwargs)
            final = f'{resultado} {nome}'
            return final
        return sua_nova_funcao
    return decorador


# a ordem que os decoradores são executados é debaixo para cima 
@parametro_decorador(nome='5')
@parametro_decorador(nome='4')
@parametro_decorador(nome='3')
@parametro_decorador(nome='2')
@parametro_decorador(nome='1')
def soma(x,y):
    return x + y


dez_mais_cinco = soma(10,5)
print(dez_mais_cinco)