# OPERAÇÕES ARITIMÉTICAS +, -, *, /, % (resto div), // (div int), ** (potência). 
# = (recebe)    == (comparação)
# Ordem de precedência: 1º (), 2º **, 3º * / // %, 4º + -
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um outro numero: '))
s = n1 + n2
sub = n1 - n2
m = n1 * n2
d = n1 / n2 
rd = n1 % n2
dint = n1 // n2
pot = n1 ** n2
print(f'{n1:d}')
print(f'A soma dos numeros {n1} e {n2} é {s}')
print(f'A subtração dos numeros {n1} e {n2} é {sub}')
print(f'A multiplicação dos numeros {n1} e {n2} é {m}')
print(f'A divisão do numero {n1} por {n2} é {d:.3f}') #DEFINIR O NÚMERO DE CASAS PÓS VÍRGULA
print(f'O resto da divisão do numeros {n1} por {n2} é {rd}')
print(f'A divisão inteira do numero {n1} por {n2} é {dint}')
print(f'A potência do numero {n1} por {n2} é {pot}')
# \n PARA QUEBRAR LINHA
# ,end=''PARA CONTINUAR LINHA MESMO MUDANDO PRINT (PODE COLOCAR QUALQUER COISA NO MEIO DO '')
