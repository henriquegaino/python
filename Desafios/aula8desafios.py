#D016
'''import math #IMPORTANDO A BIBLIOTECA INTEIRA
n = float(input('Digite um número: '))
print(f'{n} em inteiro é {math.trunc(n)} ')

from math import trunc #IMPORTANDO APENAS A FUNÇÃO
n = float(input('Digite um número: '))
print(f'{n} em inteiro é {trunc(n)} ')

#D017
import math
co = float(input('Cateto Oposto: '))
ca = float(input('Cateto Adjacente: '))
print(f'Hipotenusa = {math.hypot(co, ca):.2f}')

#D018
import math
a = float(input('Digite o Ângulo: '))
print(f'Seno = {math.sin(math.radians(a)):.2f}')
print(f'Cosseno = {math.cos(math.radians(a)):.2f}')
print(f'Tangente = {math.tan(math.radians(a)):.2f}')

#D019
import random
a1 = str(input('1º Aluno: '))
a2 = str(input('2º Aluno: '))
a3 = str(input('3º Aluno: '))
a4 = str(input('4º Aluno: '))
lista = [a1, a2, a3, a4]
escolhido = random.choice(lista)
print(f'O escolhido foi = {escolhido}')

#D020
import random
a1 = str(input('1º Aluno: '))
a2 = str(input('2º Aluno: '))
a3 = str(input('3º Aluno: '))
a4 = str(input('4º Aluno: '))
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print(f'A ordem de apresentação será: {lista}')'''

#D021.mp3

