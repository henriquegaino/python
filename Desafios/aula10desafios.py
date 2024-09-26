# D028
'''from random import randint
from time import sleep
comp = randint(0,5)
print('-=-'*20)
jog = int(input('Que número eu pensei?: '))
print('PROCESSANDO...')
sleep(3)
if(jog == comp):
    print('PARABÉNS!!!!')
else:
    print(f'Pensei no número {comp}, vc ERROU')'''

# D029
'''v = int(input('Qual a velocidade do carro?: '))
m = v - 80
multa = float(m*7)
if(v > 80):
    print('VOCÊ FOI MULTADO!!!')
    print(f'Você deverá pagar R${multa:.2f} de multa')
else:
    print('Parabéns por seguir as leis de trânsito!!')'''

# D030
'''n = int(input('Digite um número inteiro: '))
if(n%2==0):
    print(f'O nº {n} é PAR')
else:
    print(f'O nº {n} é IMPAR ')'''

# D031
'''d = float(input('Qual a distância?: '))
if d<=200:
    print(f'A viagem de {d}km custará R${d*0.50:.2f} ')
else:
    print(f'A viagem de {d}km custará R${d*0.45:.2f}')'''

# D033**
'''a = float(input('Digite o 1º número: '))
b = float(input('Digite o 2º número: '))
c = float(input('Digite o 3º número: '))

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'O maior número é {maior}')
print(f'O menor número é {menor}')'''

#D034
'''s = float(input('Qual o seu salário?: R$'))
if s > 1250:
    s = s + ((10/100)*s)
    print(f'10% de aumento. Seu novo salário é de R${s:.2f}')
else:
    s = s + ((15/100)*s)
    print(f'15% de aumento. Seu novo salário é de R${s:.2f}')'''

#D035
print('-+-'*20)
print('\033[1;31;40mANALISADOR DE TRIANGULOS\033[m')
print('-+-'*20)
a = float(input('Digite o valor do 1º segmento: '))
b = float(input('Digite o valor do 2º segmento: '))
c = float(input('Digite o valor do 3º segmento: '))

if a<b+c and b<a+c and c<a+b:
    print('Pode formar triângulo')
else:
    print('Não pode formar triângulo')


