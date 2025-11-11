"""
🧠 Exercício: Cadastro de Alunos
Crie um programa que:
- Solicite ao usuário o nome de um aluno e sua nota.
- Armazene essas informações em um dicionário, onde a chave é o nome do aluno e o valor é a nota.
- Permita cadastrar vários alunos.
- Ao final, exiba:
- Todos os alunos com suas respectivas notas.
- A média das notas.
- O aluno com a maior nota.

"""



alunos = {}

while True:
    
    try:
        nome = input('Digite o nome do aluno ou sair: ')
        if nome == 'sair':      
            break
        nota = float(input('Digite a nota do aluno: '))
    except ValueError:
        print('Voce digitou um valor invalido!')
        continue    

    alunos[nome] = nota

print()
print('Nota dos Alunos: ')
maior_nota = 0

for aluno, valor in alunos.items():
    print(f'{aluno} - {valor}')
    nota_atual = valor
    if maior_nota < nota_atual:
        maior_nota = nota_atual
        aluno_maior_nota = aluno


# calculo da media-------------------- 
soma = 0
for valores in alunos.values():
    soma += valores
media = soma / len(alunos)
# ------------------------------------


print()
print('Media de todos os Alunos:')
print(media)
print()
print('Aluno com maior nota:')
print(f'{aluno_maior_nota} - {maior_nota}')

