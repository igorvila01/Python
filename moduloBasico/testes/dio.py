# def conta_vogais(texto):
#     # TODO: Defina um conjunto de vogais tanto minúsculas quanto maiúsculas:
#     vogais = 'aeiouAEIOU'
#     # TODO: Inicialize um contador para contar as vogais:
#     contador = 0
    
#     # Iteramos pelos caracteres da string
#     for char in texto:
#         # TODO: Verifique se o caractere atual é uma vogal e incremente o valor do contador:
#         if char in vogais:
#           contador += 1
    
#     return contador

# # Solicitamos ao usuário que insira uma string
# texto = input()

# # Chamamos a função conta_vogais e exibimos o resultado
# resultado = conta_vogais(texto)
# print(f"O número de vogais na string '{texto}' é: {resultado}")


# No TODO, abaixo: Crie a função 'soma_tupla' para receber uma tupla de números inteiros como argumento:

# def soma_tupla(tupla):
#     return sum(tupla)


# if __name__ == "__main__":
#     entrada = input()
# # No "TODO", abaixo: Defina tupla para receber os números inteiros:
#     elementos = tuple(map(int, entrada.split()))
    
#     resultado = soma_tupla(elementos)
#     print(f"A soma dos elementos da tupla é: {resultado}")



# # TODO: Crie uma função 'elementos_comuns' que receba duas listas de números inteiros separados por espaço:
# def elementos_comuns(i, j):
#     set1 = set(i)
#     set2 = set(j)
#     return list(set1.intersection(set2))

# # Leitura das listas
# lista1 = input().split()
# lista2 = input().split()

# # Verifica se todas os elementos das listas podem ser convertidos para inteiros
# if all(item.isdigit() for item in lista1) and all(item.isdigit() for item in lista2):
#     comuns = elementos_comuns(lista1, lista2)
#     comuns = [int(x) for x in comuns]
#     print(f"Elementos comuns às duas listas: {comuns}")
# else:
#     print("Entrada inválida.")


def contar_caracteres(string):
#TODO: Inicialize um dicionário vazio 'contador' para armazenar as contagens de caracteres.:
    contador = {}
#TODO: Itere através de cada caractere na string string.
    for x in string:
        if x in contador:
            contador[x] += 1
        else:
            contador[x] = 1
#TODO: Para cada caractere, verifique se ele já está presente no dicionário contador:
    
    return contador

# Solicita entrada do usuário
entrada = input()
resultado = contar_caracteres(entrada)
print(resultado)