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
    print('Pergunta: ',pergunta_atual['pergunta'])
    print()
    
    opcoes = pergunta_atual['opcoes']
    for i, opcao in enumerate(opcoes):
        print(f'{i}) {opcao}')        
    print()  

    escolha = input('Escolha uma opção: ')

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)
    
    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta_atual['resposta']:
                acertou = True   
    print()
    if acertou:
        cont_acerto += 1
        print('Acertou 👍😎')
    else:
        print('Errou ❌❌😭😭')


print(f'Voce acertou {cont_acerto} \nde {len(perguntas)} perguntas!')
