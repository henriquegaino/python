# # D057
# sexo = str(input('Digite o seu sexo (M/F): ')).upper().strip()[0] #pega só a 1ª letra
# while sexo not in 'MF':
#     print('Valor inválido, digite M ou F')
#     sexo = str(input('Digite o seu sexo (M/F): ')).strip().upper()[0]
# print('Parabéns, informação correta!!')

# # D058
# from random import randint
# from time import sleep
# palpite = 1
# comp = randint(0, 5)
# print('ADIVINHE O NÚMERO')
# print('-=-'*20)
# jog = int(input('Que número eu pensei?: '))
# print('PROCESSANDO...')
# sleep(1)
# while jog != comp:
#     jog = int(input('Você errou, tente novamente: '))
#     print('PROCESSANDO...')
#     sleep(1)
#     palpite += 1
# print(f'Parabéns, você acertou depois de {palpite} tentativas. Computador = {comp}')

# if(jog == comp):
#     print('PARABÉNS!!!!')
# else:
#     print(f'Pensei no número {comp}, vc ERROU')

# # D059
# soma = 0
# n1 = float(input('Digite o 1º valor: '))
# n2 = float(input('Digite o 2º valor: '))
# opção = 0

# while opção != 5:
#     opção = int(input('\n-----MENU-----\n[1] SOMAR\n[2] SUBTRAIR\n[3] MULTIPLICAR\n[4] DIVIDIR\n[5] SAIR\n\n Escolha uma opção: '))
#     if opção == 1:
#         print('SOMA: ')
#         soma = n1 + n2
#         print(f'{n1} + {n2} = {soma}')
        
#     if opção == 2:
#         print('SUBTRAÇÃO: ')
#         sub = n1 - n2
#         print(f'{n1} x {n2} = {sub}')
      
#     if opção == 3:
#         print('MULTIPLICAÇÃO: ')
#         mult = n1 * n2
#         print(f'{n1} * {n2} = {mult}')
  
#     if opção == 4:
#         print('DIVISÃO: ')
#         div = n1 / n2
#         print(f'{n1} / {n2} = {div}')
# print('\nPROGRAMA ENCERRADO...')

# # # D060
# # #                FORMA SIMPLES
# from math import factorial
# n = int(input('Digite um nº para saber seu fatorial: '))
# fatorial = factorial(n)
# print(fatorial)
# #                FORMA DETALHADA
# from math import factorial
# n = int(input('Digite um nº para saber seu fatorial: '))
# fatorial = factorial(n)
# c = n
# print(f'{n}! = ', end = '')
# while c > 0:
#     print(f'{c}', end = '')
#     print(' x ' if c > 1 else ' = ', end = '') 
#     c -= 1
# print(fatorial)

# # D061
# print('GERADOR DE PA')
# primeiro_termo = int(input('Digite o 1º termo: '))
# razao = int(input('Digite a razão: '))
# termo = primeiro_termo
# cont = 1
# while cont <= 10:
#     print(f'{termo} =>', end =' ')
#     termo += razao
#     cont += 1
# print('FIM...')

