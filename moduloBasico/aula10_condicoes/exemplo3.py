nome = input('Qual o seu nome? ')
#  posso converter direto o input ao inves de converter depois
idade = int(input('Qual a sua idade? '))

# outra forma de converter
# idade = int(idade)

#Limite para pegar emprestimo
idade_menor = 18  #jovem
idade_maior = 30  #passou da idade

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar emprestimo.')
else:
    print(f'{nome} Não pode pegar emprestimo.')
    