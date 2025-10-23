"""
Faça um programa que pergunte a hora ao usuario e, baseando-se no horario
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# ----------------- Uma forma de se fazer - Mais completo e seguro ---------------------------------
entrada = input('Digite a hora em numeros inteiros: ')
try:
    hora = int(entrada)

    if hora >= 0 and hora <= 11:
        print(f'Bom dia!')
    elif hora >= 12 and hora <= 17:
        print(f'Boa Tarde!')
    elif hora >= 18 and hora <= 23:
        print(f'Boa Noite!')
    else:
        print('Hora informada nao esta entre 0 e 23 horas!')
except:
    print('Numero informado nao é inteiro! ')


# ------------Segunda forma de se fazer ----------------------------------
# hora = input('Digite a hora: ')

# if hora.isdigit():
#     hora_inteiro = int(hora)
#     if hora_inteiro >= 0 and hora_inteiro <= 11:
#         print(f'Bom dia!')
#     elif hora_inteiro >= 12 and hora_inteiro <= 17:
#         print(f'Boa Tarde!')
#     elif hora_inteiro >= 18 and hora_inteiro <= 23:
#         print(f'Boa Noite!')
#     else:
#         print('Hora informada nao esta entre 0 e 23 horas!') 
# else:
#     print('Numero informado nao é inteiro! ')


