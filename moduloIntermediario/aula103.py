"""
Funçoes decoradoras e decoradores 
Decorar = adicionar / remover / restringir / alterar
Funçoes decoradoras são funçoes que decoram outras funçoes 
Decoradores são usados pra fazer o Python usar as funçoes decoradoras em outras funçoes 
"""

def criar_funcao(func):
    def interna(*args, **kwargs):
        print('Vou te decorar')
        for i in args:
            e_string(i)
        resultado = func(*args, **kwargs)
        print(f'O Seu resultado foi {resultado}')
        print('Voce foi decorado')
        return resultado
    return interna

def inverte_string(texto):
    return texto[::-1]

def e_string(param):
    if not isinstance(param,str):
        raise 'Nao é um param do tipo String'


inverte_str_check_param = criar_funcao(inverte_string)

inverter = inverte_str_check_param('123')
print(inverter)