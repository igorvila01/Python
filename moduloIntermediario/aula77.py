"""
Exercicio de sistema de perguntas e respostas 
"""

perguntas = [
    {
        'pergunta': 'Quanto é 2+2?',
        'opcoes': ['1', '3', '4', '5'],
        'resposta': '4'
    },
    {
        'pergunta': 'Quanto é 5*5?',
        'opcoes': ['25', '55', '10', '51'],
        'resposta': '25'
    },
    {
        'pergunta': 'Quanto é 10/2?',
        'opcoes': ['4', '5', '2', '1'],
        'resposta': '5'
    }
]

cont_acerto = 0
for sep_dicionario in perguntas:
    print(sep_dicionario['pergunta'])
    cont = 0
    for i in sep_dicionario['opcoes']:
        print(f'{cont}) {i}')
        cont += 1
    print()    
    resposta = input('Selecione sua resposta: ')

    try:
        resposta = int(resposta)
        if sep_dicionario['opcoes'][resposta] == sep_dicionario['resposta']:
            print('Voce acertou!')
            cont_acerto += 1
        else: 
            print('Voce errou!')
    except ValueError:
        print('Resposta Invalida!')

print(f'Voce acertou {cont_acerto} de {len(perguntas)} perguntas!')
