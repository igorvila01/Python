"""
Variaveis - armazenar espaços com dados na memoria
Iniciar somente com letra, mas pode conter numeros
Nome de variavel composto, separar por _
Sempre com letras minusculas

"""
from math import trunc

nome = 'Igor Vila'
idade = 30
altura = 1.87
e_maior = idade > 18
# data_1 = false
# data_atual = 2025
peso = 98
imc = peso / (altura**2)

print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('É Maior:', e_maior)

print(idade * altura)

print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)
if imc < 18.5:
    print(imc, 'Magreza')
elif imc >=18.5 and imc <=24.9:
    print(imc, 'Normal')
elif imc >=25. and imc <29.9:
    print(imc, 'Sobrepeso')
elif imc >=30. and imc <39.9:
    print(imc, 'Obesidade')
else:
    print(imc, 'Obesidade Grave')
