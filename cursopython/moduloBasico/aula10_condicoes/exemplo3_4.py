primeiro_valor = input("Digite um valor: ")
segundo_valor = input("Digite outro valor: ")
primeiro_valor = int(primeiro_valor)
segundo_valor = int(segundo_valor)

if primeiro_valor == segundo_valor:
    print(f"Os valores são iguais primeiro valor = {primeiro_valor}" \
          f" segundo valor = {segundo_valor}")
elif primeiro_valor > segundo_valor:
    print(f"O {primeiro_valor} é maior que o {segundo_valor}")
else:
    print(f"O {segundo_valor} é maior que o {primeiro_valor}")

    