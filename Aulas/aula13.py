# while ESTRUTURA DE REPETIÇÃO
# QUANDO NÃO SE SABE O LIMITE
c = 1
n = 0
n = int(input(f'Digite o {c}º número: '))
soma = n
while n != 0: #CONDIÇÃO DE PARADA
    c += 1
    n = int(input(f'Digite o {c}º número: '))
    soma += n
print(soma)

# EXEMPLO******
# while não  chegar na maçã:
#     if se tiver chão:
#         anda
#     if se tiver buraco:
#         pula
#     if se tiver moeda:
#         pega
# pegar maçã

# c = 1
# n = int(input('Digite um número: '))
# while c <= n:
#     print(c, end=' ')
#     c += 1

par = impar = 0
n = 1
while n != 0:
    n = int(input('Digite um nº: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'{par} números pares\n{impar} números impares')