#D072
# cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
#       'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
#         'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
# while True:
#     n = int(input('Digite um número entre 0 e 20: '))
#     if 0 <= n <= 20:
#         break
#     print('Tente novamente...')
# print(f'Você digitou o número {cont[n]}')

#D073
# cidades = ('São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Brasília', 'Salvador',
#             'Fortaleza', 'Curitiba', 'Manaus', 'Recife', 'Porto Alegre', 'Belém', 'Goiânia',
#               'São Luís', 'Maceió', 'Natal', 'Campo Grande', 'João Pessoa', 'Cuiabá', 'Aracaju', 'Florianópolis')
# print(f'As cinco primeiras cidades são {cidades[0:5]}')
# print(f'As últimas 4 cidades são {cidades[-4:]}')
# print(f'As cidades em ordem alfabética são {sorted(cidades)}')
# print(f'Salvador está na posição {cidades.index("Salvador")}')

#D074
# from random import randint
# numeros = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10),)
# for n in numeros:
#     print(f'{n}', end='   ')
# print(f'\nO maior valor é {max(numeros)}')
# print(f'O menor valor é {min(numeros)}')

#D075
# n = (int(input('Digite o 1 numero: ')),int(input('Digite o 2 numero: ')),
#      int(input('Digite o 3 numero: ')),int(input('Digite o 4 numero: ')))
# print(f'Voce digitou os valores {n}')
# print(f'O valor 9 apareceu {n.count(9)} vezes')
# if 3 in n:
#     print(f'O valor 3 apareceu na {n.index(3)+1} posição')
# else:
#     print('O numero 3 não apareceu')
# for c in n:
#     if c % 2 == 0:
#         print(f'{c} é par')

#D076
# produtos = ('Caderno', 25.5,
#             'Borracha', 7.9,
#             'Mochila', 108.5)
# print('_'*40)
# print(f'{"LISTAGEM DE PREÇOS":^40}')
# print('_'*40)
# for pos in range(0,len(produtos)):
#     if pos % 2 == 0:
#         print(f'{produtos[pos]:.<30}', end='')
#     else:
#        print(f'R${produtos[pos]:>5.2f}') 

#D077

# palavras = ('casa', 'carro', 'flor', 'livro', 'porta', 'mesa', 'cadeira',
#              'janela', 'computador', 'telefone', 'telefone', 'cachorro', 'gato',
#               'arvore', 'sol', 'lua', 'rio', 'mar', 'estrada', 'cidade')
# for p in palavras:
#     print(f'\nNa palavra {p.upper()} temos', end=' ')
#     for letra in p:
#         if letra.lower() in 'aeiou':
#             print(letra, end=' ')

