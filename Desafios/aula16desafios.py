#D084
# dados = list()
# pessoas =list()
# while True:
#     dados.append(str(input('Digite o nome: ')))
#     dados.append(float(input('Digite o peso (KG): ')))
#     pessoas.append(dados[:])
#     condição = str(input('Deseja continuar? [s/n]: ')).lower()
#     dados.clear()
#     if condição == 'n':
#         break
#     pesos = list()
# print(f'ao todo voce cadastrou {len(pessoas)} pessoa(s)')
# for elemento in pessoas:
#     pesos.append(elemento[1])
# print(f'O menor peso foi {min(pesos)}')
# print(f'O maior peso foi {max(pesos)}')

#D085
num = [[],[]] #0 e 1

for c in range(1,8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
num[0].sort()
num[1].sort()
print(f'Os valores pares são: {num[0]}')
print(f'Os valores impares são: {num[1]}')

#D086
matriz = [[0,0,0],[0,0,0],[0,0,0]]

for l in matriz:
    for c in matriz:
        matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]: '))