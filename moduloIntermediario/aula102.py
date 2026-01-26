# Variaveis Livres + nonlocal



def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_a_concatenar=''):
        # nonlocal, utilizado para alterar variaveis livres que esta dentro de outro escopo
        nonlocal valor_final
        valor_final += valor_a_concatenar
        return valor_final

    return interna 

c= concatenar('a')
print(c('b'))
print(c('c'))
print(c('d'))
final = c()
print(final)