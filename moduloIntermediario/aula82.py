def executa(funcao, *args):
    return funcao(*args)

def soma(x,y):
    return x+y
# Essa funcao lambda é como se fosse utilizar a função soma 
print(executa (lambda x, y: x + y, 1,2))

def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

# Função lambda para utilizar cria multiplicador.
# Lembrando que lambda é para coisas rapidas, e nao para coisas complexas, pois nao fica legivel 
duplica = executa(lambda m: lambda n: n * m, 2)
print(duplica(5))

# utilizando args para fazer uma soma de varios argumentos
print(executa(lambda *args: sum(args), 1,2,3,4))