#1
# n1 = int(input('Digite o 1º número: '))
# n2 = int(input('Digite o 2º número: '))
# if n1>n2:
#     print(f'{n1}>{n2}')
#elif n1==n2:
#   print('Os números são iguais')
# else:
#     print(f'{n2}>{n1}')

#2
# n = float(input('Digite um valor: '))
# if n > 0:
#     print('O valor é positivo')
# else:
#     print('O valor é negativo')

#3
# Lista de perguntas
# perguntas = [
#     "Telefonou para a vítima? (sim/não): ",
#     "Esteve no local do crime? (sim/não): ",
#     "Mora perto da vítima? (sim/não): ",
#     "Devia para a vítima? (sim/não): ",
#     "Já trabalhou com a vítima? (sim/não): "
# ]

# sim = 0

# for pergunta in perguntas:
#     resposta = str(input(f'{pergunta}')).strip().lower()
#     if resposta == 's':
#         sim+=1
# if sim == 2:
#     classificacao = "Suspeita"
# elif 3 <= sim <= 4:
#     classificacao = "Cúmplice"
# elif sim == 5:
#     classificacao = "Assassino"
# else:
#     classificacao = "Inocente"

# print(f"Classificação: {classificacao}")

# #4
# morango_ate_5kg = 2.50
# morango_acima_5kg = 1.80
# maça_ate_5kg = 2.20
# maça_acima_5kg = 1.50

# morango_kg = float(input('Digite a quantidade de Morangos (KG): '))
# maça_kg = float(input('Digite a quantidade de Maçã (KG): '))

# if morango_kg <= 5:
#     valor_morango = morango_kg*morango_ate_5kg
# else:
#     valor_morango = morango_kg*morango_acima_5kg
# if maça_kg <= 5:
#     valor_maça = maça_kg*maça_ate_5kg
# else:
#     valor_maça = maça_kg*maça_acima_5kg

# valor_total = valor_maça + valor_morango

# if valor_total > 25 or (maça_kg+morango_kg)>8:
#     valor_total = valor_total*0.90
# print(f'O valor total é: R${valor_total:.2f}')

# Preços das carnes ########################
# preco_file_duplo_ate_5kg = 4.90
# preco_file_duplo_acima_5kg = 5.80
# preco_alcatra_ate_5kg = 5.90
# preco_alcatra_acima_5kg = 6.80
# preco_picanha_ate_5kg = 6.90
# preco_picanha_acima_5kg = 7.80

# # Solicita o tipo de carne
# tipo_carne = input("Digite o tipo de carne (File Duplo, Alcatra, Picanha): ").strip().lower()
# # Solicita a quantidade de carne em kg
# quantidade_carne = float(input("Digite a quantidade de carne (em Kg): "))
# # Solicita o tipo de pagamento
# tipo_pagamento = input("O pagamento será no cartão Tabajara? (sim/não): ").strip().lower()

# # Inicializa variáveis
# preco_carne = 0

# # Determina o preço da carne com base no tipo e quantidade
# if tipo_carne == "file duplo":
#     if quantidade_carne <= 5:
#         preco_carne = preco_file_duplo_ate_5kg
#     else:
#         preco_carne = preco_file_duplo_acima_5kg
# elif tipo_carne == "alcatra":
#     if quantidade_carne <= 5:
#         preco_carne = preco_alcatra_ate_5kg
#     else:
#         preco_carne = preco_alcatra_acima_5kg
# elif tipo_carne == "picanha":
#     if quantidade_carne <= 5:
#         preco_carne = preco_picanha_ate_5kg
#     else:
#         preco_carne = preco_picanha_acima_5kg
# else:
#     print("Tipo de carne inválido!")
#     exit()

# # Calcula o preço total
# preco_total = quantidade_carne * preco_carne

# # Inicializa valor do desconto
# desconto = 0

# # Aplica desconto de 5% se o pagamento for no cartão Tabajara
# if tipo_pagamento == "sim":
#     desconto = preco_total * 0.05
#     preco_final = preco_total - desconto
# else:
#     preco_final = preco_total

# # Gera o cupom fiscal
# print("\n=== CUPOM FISCAL ===")
# print(f"Tipo de carne: {tipo_carne.capitalize()}")
# print(f"Quantidade de carne: {quantidade_carne:.2f} Kg")
# print(f"Preço total: R$ {preco_total:.2f}")
# print(f"Tipo de pagamento: {'Cartão Tabajara' if tipo_pagamento == 'sim' else 'Outro'}")
# print(f"Valor do desconto: R$ {desconto:.2f}")
# print(f"Valor a pagar: R$ {preco_final:.2f}")
