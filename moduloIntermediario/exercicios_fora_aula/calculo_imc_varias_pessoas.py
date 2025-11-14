"""
🧩 Desafio: IMC de um grupo de pessoas
Crie um programa que:
- Peça ao usuário quantas pessoas serão avaliadas.
- Para cada pessoa, solicite o nome, peso e altura.
- Use funções para:
- Calcular o IMC
- Classificar o IMC
- Armazene os dados em uma lista de dicionários, como:
[
  {'nome': 'Ana', 'imc': 22.5, 'classificacao': 'Peso Normal'},
  {'nome': 'Carlos', 'imc': 31.2, 'classificacao': 'Obesidade Grau 1'},
  ...
]

- Ao final, exiba um relatório com todos os nomes, IMCs e classificações
💡 Dica extra
Você pode adicionar uma função chamada exibir_relatorio(lista) que percorre a lista e imprime os dados formatados.
"""

def calcular_imc(peso, altura):
    peso = float(peso)
    altura = float(altura)
    imc = peso/(altura**2)
    return imc

def classificar_imc(imc):
    imc = float(imc)
    if imc < 18.5:
        return 'Abaixo do peso'
    elif imc >= 18.5 and imc <= 24.9:
        return 'Peso Normal'
    elif imc >= 25 and imc <= 29.9:
        return 'Sobrepeso'
    elif imc >= 30 and imc <= 34.9:
        return 'Obesidade Grau 1'
    elif imc >= 35 and imc <= 39.9:
        return 'Obesidade Grau 2'
    else:
        return 'Obesidade Grau 3'


while True:
    try:
        qtd_pessoas = int(input('Digite a quantidade de pessoas que serao avaliadas: '))
        break
    except ValueError:
        print('❌Digite um numero inteiro valido! ')
        continue

pessoas = []
pessoa = {}
for i_pessoa in range(qtd_pessoas):
    while True:
        try:
            nome = str(input('Digite o nome da pessoa: '))
            peso = float(input('Digite o peso da pessoa: '))
            altura = float(input('Digite a altura da pessoa: '))
            pessoa['nome'] = nome
            pessoa['peso'] = peso
            pessoa['altura'] = altura

            imc = calcular_imc(peso, altura)
            pessoa['imc'] = imc
            classificacao = classificar_imc(imc)
            pessoa['classificacao'] = classificacao

            pessoas.append(pessoa)
            break
        except ValueError:
            print('❌Entrada Inválida!')
            continue

print(f'Nome = {pessoas[i_pessoas]['nome']}, IMC: {pessoas[i_pessoas]['imc']}, Classificação: {pessoas[i_pessoas]['classificacao']}')


        
    
    
