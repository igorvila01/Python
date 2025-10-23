nome = 'Igor Luiz Vila'
idade = 30
altura = 1.88
peso = 98.0
ano_atual = 2025
ano_nascimento = ano_atual-idade
imc = peso / (altura**2)

print(f"{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg."
      f"\nO IMC de {nome} é {imc:.2f}."
      f"\n{nome} nasceu em {ano_nascimento}")
