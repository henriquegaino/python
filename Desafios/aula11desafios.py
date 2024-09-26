# D036
'''valor = float(input('Qual o valor da casa?: '))
salario = float(input('Qual o salário?: '))
anos = float(input('Quantos anos parcelar?: '))
parcela = valor/(anos*12)
por = (30/100)*salario
if parcela > por:
    print('Emprestimo NEGADO')
else:
    print('Emprestimo ACEITO')
    print(f'A parcela será de R${parcela:.2f} durante {anos*12} meses ({anos} anos)')'''

# D037
'''n = int(input('Digite um número: '))
print(Qual base deseja converter?:
	
(1) BINÁRIO
(2) OCTAL
(3) HEXADECIMAL
)
base = int(input('Digite 1, 2 ou 3: '))
if base == 1:
    print(f'O número {n} em Binário é {bin(n)[2:]}')
elif base == 2:
    print(f'O número {n} em Octal é {oct(n)[2:]}')
elif base == 3:
    print(f'O número {n} em Hexadecimal é {hex(n)[2:]}')
else:
    print('Opcao inválida. TENTE NOVAMENTE...')'''

# D038
'''n1 = float(input('Digite 1º número: '))
n2 = float(input('Digite 2º número: '))
if n1>n2:
	print(f'O número {n1} é maior que o número {n2}')
	
elif n1<n2:
	print(f'O número {n1} é menor que o número {n2}')

else:
	print('Os números são iguais')'''

# D039
'''ano = int(input('Digite o seu ano de nascimento: '))
idade = 2024-ano
alistar = idade - 18
if idade > 18:
    s = int(input('Você se alistou?:\n\n(1)SIM\n(2)NÃO\n\nDigite o nº da opção:' ))
    if s == 1:
        print(f'Você tem {idade} anos e se alistou á {alistar} anos. TUDO OK!!')
    else:
        print(f'Vá se alistar o mais rápido possível, você já tem {idade} anos e está atrasado á {alistar} anos')
elif idade == 18:
    print('Você deve se alistar esse ano')
else:
    print(f'Você tem {idade} e deve se alistar daqui á {alistar*-1} ano(s)')'''

# D040
'''n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1+n2)/2

if media < 5:
    print(f'REPROVADO, sua média é {media}')
elif media == 7 or media > 7:
    print(f'APROVADO, sua média é {media}')
else:
    print(f'RECUPERAÇÃO, sua média é {media}')'''

# D041
'''ano = int(input('Digite seu ano de nascimento: '))
idade = 2024 - ano

if idade<=9:
    print('Atleta MIRIM')
elif idade <= 14:
    print('Atleta INFANTIL')
elif idade <= 19:
    print('Atleta JÚNIOR')
elif idade <= 25:
    print('Atleta SÊNIOR')
elif idade > 25:
    print('Atleta MASTER')
else:
    print('Valor não encontrado, digite novamente')'''

# D042
'''print('-+-'*20)
print('\033[1;31;40mANALISADOR DE TRIANGULOS\033[m')
print('-+-'*20)
a = float(input('Digite o valor do 1º segmento: '))
b = float(input('Digite o valor do 2º segmento: '))
c = float(input('Digite o valor do 3º segmento: '))

if a<b+c and b<a+c and c<a+b:
    print('Pode formar triângulo')
    if a == b== c:
        print('Triangulo EQUILATERO')
    elif a != b != c != a:
        print('Triangulo ESCALENO')
    else: 
        print('Triangulo ISOSCELES')
else:
    print('Não pode formar triângulo')'''

# D044
'''v = float(input('Qual o valor do produto?: R$'))
pag = int(input('Qual será a forma de pagamento?:\n\n(1)DINHEIRO\n(2)CARTÃO DÉBITO\n(3)2xCRÉDITO\n(4)3x ou mais CRÉDITO\nEscolha o nº: '))
if pag == 1:
    v = v - ((10/100)*v)
    print(f'Você pagará R${v:.2f}')
elif pag == 2:
    v = v - ((5/100)*v)
    print(f'Você pagará R${v:.2f}')
elif pag == 3:
    print(f'Você pagará R${v:.2f}')    
elif pag == 4:
    v = v + ((20/100)*v)
    print(f'Você pagará R${v:.2f}')'''

# D045
'''from random import randint
item = ('Pedra', 'Papel', 'Tesoura')
print('-=-'*20)
eu = int(input('(0)PEDRA\n(1)PAPEL\n(2)TESOURA\nEscolha um número: '))
if eu != 0 and eu != 1 and eu != 2:
    print('JOGADA INVÁLIDA')
else:
    pc = randint(0, 2)
    print(f'Computador = {item[pc]}\nVocê = {item[eu]}')

    if pc == eu:
        print('EMPATE')
    elif eu == 0:
        if pc == 1:
            print('O computador VENCEU')
        elif pc == 2:
            print('Você VENCEU')
    elif eu == 1:
        if pc == 2:
            print('O computador VENCEU')
        elif pc == 0:
            print('Você VENCEU')
    elif eu == 2:
        if pc == 0:
            print('O computador VENCEU')
        elif pc == 1:
            print('Você VENCEU')'''
