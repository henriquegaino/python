# MANIPULANDO TEXTO (CADEIA DE STRING)
# *FATIAMENTO frase = 'Curso em vídeo' frase[9] / frase[0:5](5-1) / frase[0:10:2](2-1 pulando 1 letra por vez)
frase = 'O Henrique estudou programação'
print(f'{frase[11:18]}')
print(f'{frase[:30]}')
print(f'{frase[2:30:2]}')
print(f'{frase[::4]}')

# *ANÁLISE
frase = 'O Henrique estudou programação'
print(f'{len(frase)}') #contar quantos caractéres 
print(f'{frase.count('e')}') #mostra quantas vezes o valor definido aparece
print(f'{frase.count('e',0,20)}') #mostra quantas vezes o valor definido aparece do caractere 0 ao 20
print(f'{frase.find('rique')}') #indica em q posição a frase começa
print(f'{'Henrique' in frase}')  # pesquisar palavra na frase

# *TRANSFORMAÇÃO
frase = 'O Henrique estudou programação'
# Muda a sequência de caractéres indicada
print(f'{frase.replace('O Henrique', 'Júlia')}')
print(f'{frase.upper()}')  # Deixa tudo em MAIÚSCULO
print(f'{frase.lower()}')  # Deixa tudo em MINÚSCULO
print(f'{frase.capitalize()}')  # Deixa com a 1ª letra MAIÚSCULA
# Quebra os espaçoes e deixa as primeiras letras maiúsculas
print(f'{frase.title()}')
# Remove os primeiros e últimos espaços (MUITO USADO PARA COLOCAR EMAIL E SENHA SEM ERRO) rstrip tira só os últimos / lstrip tira os da esquerda
print(f'{frase.strip()}')

# *DIVISÃO E JUNÇÃO
frase = 'O Henrique estudou programação'
print(f'{frase.split()}') #Divide os espaços 01234 012 0123 012345
print(f'{' bonitão '.join(frase.split())}') # Junta os espaços com o caractere definido
