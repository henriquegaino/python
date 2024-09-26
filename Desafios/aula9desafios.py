# D022
'''nome = str(input('Digite seu nome completo: ')).strip() #strip para separar cada caractere
print(f'Maiúsculo: {nome.upper()}')
print(f'Minúsculo: {nome.lower()}')
print(f'Seu nome tem {len(nome)-nome.count(' ')} letras') #count conta quantos espaços foram digitados
print(f'Seu 1º nome tem {nome.find(' ')} letras') #OU SEPARANDO EM LISTA
nome1 = nome.split() 
print(f'Seu 1º nome tem {len(nome1[0])} letras')'''

#D023 *
'''n = int(input('Digite um número com 4 dígitos: '))
n1 = str(n)
print(f'Unidade: {n1[3]}')
print(f'Dezena: {n1[2]}')
print(f'Centena: {n1[1]}')
print(f'Milhar: {n1[0]}')
#OU
n = int(input('Digite um número com 4 dígitos: '))
print(f'Unidade: {n // 1 % 10}')
print(f'Dezena: {n // 10 % 10}')
print(f'Centena: {n // 100 % 10}')
print(f'Milhar: {n // 1000 % 10}')'''

#D024
'''c = str(input('Qual cidade vc nasceu?: ')).strip()
print(c[:3].upper() == 'SÃO')

c = str(input('Qual cidade vc nasceu?: '))
if('São' in c):
    print("Cidade Cadastrada")
else:
    print('Cidade NÃO cadastrada')'''

#D026
'''f = str(input('Digite uma frase: '))
l = str(input('Digite a letra: '))
print(f'A letra ({l}) aparece {f.count(l)} vezes na frase')
print(f'A letra ({l}) aparece na posição {f.find(l)+1} a 1ª vez')
print(f'A letra {l} aparece na posição {f.rfind(l)+1} na última vez')'''

#D027
'''n = str(input('Digite um nome completo: ')).strip()
nome = n.split()
print(f'O 1º nome é: {nome[0]}')
print(f'O último nome é: {nome[len(nome)-1]}')'''