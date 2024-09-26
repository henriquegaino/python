#D078
# lista = []
# for x in range(1,6):
#     lista.append(int(input(f'Digite o {x}º valor: ')))
# print(lista)
# print(f'O maior valor da lista é {max(lista)}')
# print(f'O menor valor da lista é {min(lista)}')

#D079 EU FIZ
# lista = []
# c=1
# while True:
#     n = int(input(f'Digite o {c}º número: '))
#     c+=1
#     if n not in lista:
#         lista.append(n)
#         print('Valor adicionado com sucesso!')
#     else:
#         print('Valor duplicado, não será adicionado...')
#         c-=1
#     condição = str(input('Deseja continuar? [S/N]: ')).lower()
#     if condição not in 'sn':
#         print('Valor indefinido, digite apenas S/N: ')
#     elif condição == 'n':
#         break
# lista.sort()
# print(lista)

#CHAT GPT FEZ##########################################################
# lista = []
# c = 1

# while True:
#     while True:
#         try:
#             n = int(input(f'Digite o {c}º número: '))
#             break  # Sai do loop se a conversão for bem-sucedida
#         except ValueError:
#             print("Valor não numérico, digite novamente")

#     if n not in lista:
#         lista.append(n)
#         print('Valor adicionado com sucesso!')
#     else:
#         print('Valor duplicado, não será adicionado...')
#         c -= 1

#     while True:
#         condicao = input('Deseja continuar? [S/N]: ').strip().lower()
#         if condicao in 'sn' and len(condicao) == 1:
#             break
#         else:
#             print('Valor indefinido, digite apenas S/N: ')

#     if condicao == 'n':
#         break

#     c += 1

# lista.sort()
# print(lista)

#D080
#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
#  já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
# lista = []
# for c in range (1,6):
#     n = int(input(f'Digite o {c}º número: ')) 
#     if c == 1 or n > lista[len(lista)-1]:
#         lista.append(n)
#         print('O número foi adicionado no final da lista...')
#     else:
#         pos = 0
#         while pos < len(lista):
#             if n <= lista[pos]:
#                 lista.insert(pos, n)
#                 print(f'Número adicionado na posição {pos}...')
#                 break
#         pos+=1        
# print(lista)

#D081
# lista = []
# c=1
# while True:
#     n = int(input(f'Digite o {c}º valor: '))
#     c+=1
#     lista.append(n)
#     condição = str(input('Deseja continuar? [S/N]: ')).lower()
#     if condição == 'n':
#         break
# print(lista)
# print(f'Foram digitados {len(lista)} números')
# lista.sort(reverse=True)
# print(f'A lista em valor decrescente é {lista}')
# if '5' in lista:
#     print(f'O valor 5 aparece {lista.count(5)} vezes')
# else:
#     print('O valor 5 não aparece na lista')

#D082
# lista = []
# listapar = []
# listaimpar = []
# c=1
# while True:
#     n = int(input(f'Digite o {c}º valor: '))
#     c+=1
#     lista.append(n)
#     if n % 2 == 0:
#         listapar.append(n)
#     else:
#         listaimpar.append(n)
#     condição = str(input('Deseja continuar? [S/N]: ')).lower()
#     if condição == 'n':
#         break
# print(lista)
# print(listapar)
# print(listaimpar)

#D083
# p1 = p2 = 0
# e = str(input('Digite uma expressão: '))
# p2 = e.count(')')
# p1 = e.count('(')
# if p1 == p2:
#     print('A expressão está correta')
# else:
#     print('A expressão está errada')

lista = []
e = str(input('Digite uma expressão: '))
for s in e:
    if s == '(':
        lista.append('(')
    elif s == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('A Exp está correta')
else:
    print('ERRADO')
print(lista)
        

