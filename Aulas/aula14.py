#TUPLAS

# lanche = 'hamburguer','suco','pizza','pudim'

# for c in range(0,len(lanche)): #Forma diferente usando o range
#     print(f'eu vou comer {lanche[c]} na posição {c}')

# # for c in lanche:
# #     print(c)

# print(sorted(lanche)) #Coloca a tupla em ordem alfabética
# # print('##Comi muito!##')

# a = (2,5,4)
# b = (5,8,1,2)
# c = a + b
# print(c)
# print(c.count(5)) #Quantas vezes o número aparece na tupla
# print(c.index(8)) #Mostra em qual posição está o número

######RESUMO **TUPLA** CHAT GPT#########################################################
# Definindo uma tupla de produtos eletrônicos
produtos_eletronicos = ('celular', 'notebook', 'tablet', 'smartwatch', 'fones de ouvido')

# Imprimindo a tupla completa
print(f"Tupla de Produtos Eletrônicos: {produtos_eletronicos}")

# Acessando elementos da tupla pelo índice
print(f"Primeiro produto: {produtos_eletronicos[0]}")
print(f"Último produto: {produtos_eletronicos[-1]}")

# Iterando sobre os elementos da tupla
print("Produtos Eletrônicos:")
for produto in produtos_eletronicos:
    print(produto)

# Verificando o tamanho da tupla
print(f"Número de produtos eletrônicos: {len(produtos_eletronicos)}")

# Verificando a existência de um elemento na tupla
if 'tablet' in produtos_eletronicos:
    print("O tablet está na lista de produtos eletrônicos.")
else:
    print("O tablet não está na lista de produtos eletrônicos.")

# Contando o número de ocorrências de um elemento na tupla
numero_de_fones = produtos_eletronicos.count('fones de ouvido')
print(f"Número de fones de ouvido na tupla: {numero_de_fones}")

# Encontrando o índice de um elemento na tupla
indice_notebook = produtos_eletronicos.index('notebook')
print(f"O notebook está no índice: {indice_notebook}")

# Desempacotando uma tupla
produto1, produto2, produto3, produto4, produto5 = produtos_eletronicos
print(f"Desempacotando a tupla: {produto1}, {produto2}, {produto3}, {produto4}, {produto5}")


######RESUMO **LISTA** CHAT GPT#########################################################
# Criando uma lista de frutas
frutas = ['maçã', 'banana', 'laranja', 'manga', 'uva']

# Imprimindo a lista completa
print(f"Lista de Frutas: {frutas}")

# Acessando elementos da lista pelo índice
print(f"Primeira fruta: {frutas[0]}")
print(f"Última fruta: {frutas[-1]}")

# Modificando um elemento da lista
frutas[1] = 'morango'
print(f"Lista após modificação: {frutas}")

# Adicionando um elemento no final da lista
frutas.append('abacaxi')
print(f"Lista após adicionar um elemento: {frutas}")

# Inserindo um elemento em uma posição específica
frutas.insert(2, 'kiwi')
print(f"Lista após inserir um elemento: {frutas}")

# Removendo um elemento pelo valor
frutas.remove('manga')
print(f"Lista após remover um elemento: {frutas}")

# Removendo o último elemento da lista
ultima_fruta = frutas.pop()
print(f"Lista após remover o último elemento: {frutas}")
print(f"Última fruta removida: {ultima_fruta}")

# Removendo um elemento por índice
fruta_removida = frutas.pop(1)
print(f"Lista após remover o elemento no índice 1: {frutas}")
print(f"Fruta removida do índice 1: {fruta_removida}")

# Encontrando o índice de um elemento
indice_uva = frutas.index('uva')
print(f"O índice da uva na lista: {indice_uva}")

# Contando o número de ocorrências de um elemento
numero_de_macas = frutas.count('maçã')
print(f"Número de maçãs na lista: {numero_de_macas}")

# Ordenando a lista
frutas.sort()
print(f"Lista após ordenação: {frutas}")

# Invertendo a ordem da lista
frutas.reverse()
print(f"Lista após reversão: {frutas}")

# Copiando a lista
frutas_copia = frutas.copy()
print(f"Cópia da lista de frutas: {frutas_copia}")

# Limpando todos os elementos da lista
frutas.clear()
print(f"Lista após limpar todos os elementos: {frutas}")
