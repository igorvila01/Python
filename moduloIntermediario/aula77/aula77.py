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
for pergunta_atual in perguntas:
    print(pergunta_atual['pergunta'])
    indice_opcao = 0
    for i in pergunta_atual['opcoes']:
        print(f'{indice_opcao}) {i}')
        indice_opcao += 1
    print()    
    resposta = input('Selecione sua resposta: ')

    try:
        resposta = int(resposta)
        if pergunta_atual['opcoes'][resposta] == pergunta_atual['resposta']:
            print('Voce acertou!')
            cont_acerto += 1
        else: 
            print('Voce errou!')
    except ValueError:
        print('Resposta Invalida!')

print(f'Voce acertou {cont_acerto} de {len(perguntas)} perguntas!')
