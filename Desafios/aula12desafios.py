# # D046
# from time import sleep
# for x in range(10,0,-1):
#     print(x)
#     sleep(1)
# print('Feliz Ano Novo!!!')

# # D047
# for x in range(2,51,2):
#     print(x, end=' ')

# # D048
# s = 0
# n = int(input('Digite um número: '))
# for c in range(1,n+1):
#     if c % 3 == 0:
#         s = s+ c
# print(f'A soma entre os múltiplos de 3 do 1 até o {n} é = {s}')

# # D049
# n = int(input('Digite um número: '))
# for c in range(1,11):
#     print(f'{n}x{c} = {n*c}')
#     c = c+1

# # D050
# s = 0
# for x in range(1,7):
#     n = int(input(f'Digite o {x}º número: '))
#     if n % 2 == 0:
#         s = n + s 
#     else:
#         print(f'O número {n} não é PAR')
# print(f'A SOMA DOS NÚMEROS PARES É {s}')

# # D051
# primeiro_termo = float(input("Informe o primeiro termo da PA: "))
# razao = float(input("Informe a razão da PA: "))
# # Calcula e exibe os 10 primeiros termos da PA
# print("Os 10 primeiros termos da PA são:")
# for x in range(10):
#     termo_atual = primeiro_termo + x * razao
#     print(f"Termo {x + 1}: {termo_atual}")

# # D052 NÚMEROS PRIMOS *******
# n = int(input('Digite um nº inteiro: ')) #Num primo só é divisível por 1 e por ele mesmo
# div = 0
# for c in range(1, n+1):
#     if n % c == 0:
#         print('\033[92m', end = ' ') #amarelo
#         div += 1
#     else:
#         print('\033[31m', end = ' ') #vermelho
#     print(c, end =' ')
# print(f'\n\033[33mO nº {n} foi divisível {div} vezes\033[m')
# if div == 2:
#     print('\033[92mÉ PRIMO\033[m')
# else:
#     print('\033[31mNÃO É PRIMO\033[m')

# # D053
# frase = input("Qual a frase?: ").upper().replace(" ", "")
# print(f'A frase {frase} é {frase[::-1]} ao contrário')
# if frase == frase[::-1]:
#     print("A frase é um palíndromo")
# else:
#     print("A frase não é um palíndromo")

# # D054
# c = m =0
# for x in range(1,8):
#     ano = int(input(f'Digite o {x}º ano de nascimento: '))
#     idade = 2024-ano
#     if idade >= 18:
#         c += 1
#     else:
#         m+=1
# print(f'{c} estão na maioridade e {m} estão na minoridade')

# # D055 **
# maior = menor = 0
# for x in range(1,6):
#     peso = float(input(f'Digite o {x}º peso: '))
#     if x == 1:  #estudar novamente essa parte
#         maior = peso
#         menor = peso
#     else: 
#         if peso > maior:
#             maior = peso
#         if peso < menor:
#             menor = peso
# print(f'O maior peso foi {maior}kg')
# print(f'O menor peso foi {menor}kg')

# D056 ******
soma_idade = media_idade = maior_idade_homem = c = 0
nomevelho = ''

for p in range(1, 5):

    print(f'======= {p}ª Pessoa =======')
    nome = str(input(f'Nome: ')).title().strip()
    idade = int(input(f'Idade: '))
    sexo = str(input(f'Sexo (M/F): ')).strip().upper()
    soma_idade += idade

    if p == 1 and sexo == 'M':
        maior_idade_homem = idade
        nomevelho = nome 

    if sexo == 'M' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nomevelho = nome

    if sexo == 'F' and idade < 20:
        c += 1 

media_idade = soma_idade/4
print(f'A média de idade do grupo é de {media_idade} anos.')
print(f'O homem mais velho tem {maior_idade_homem} anos e se chama {nomevelho}.')
print(f'{c} mulheres tem menos de 20 anos.')