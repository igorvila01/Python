import json

pessoa = {
    'nome': 'Igor Luiz',
    'sobrenome': 'Vila',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 35},
    ],
    'altura': 1.87,
    'idade': 31,
    'dev': True,
    'nada': None
}

# ensure_ascii = vai deixar os arquivos com os seus devidos caracteres especiais, como acentuação por exemplo 
with open('aula117.json', 'w') as arquivo:
    json.dump(pessoa, 
              arquivo, 
              ensure_ascii=False, # ensure_ascii = vai deixar os arquivos com os seus devidos caracteres especiais, como acentuação por exemplo 
              indent=2) # indent= formata o texto json , esse numero vai definir a quantidade de espaços, caso queira tabulação coloque "\t"