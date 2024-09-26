#LISTA PT.1
# n = [2,5,9,1]
# print(n)
# n[2]=3 #Modificar valor
# n.append(7) #Adicionar valor no final
# n.insert(2,0)
# print(n)
# n.sort() #Organiza lista
# print(n)
# n.sort(reverse=True) #Inverte organização lista
# print(n)
# n.pop() #Elimina o último valor
# n.pop(2) #Elimina o elemento 2 (0,1,2)
# print(f'Essa lista tem {len(n)} elementos') #Qnts elementos tem na lista

lista = []
for x in range(1,6):
    lista.append(int(input(f'Digite o {x}º valor: ')))
print(f'O maior valor da lista é {max(lista)}')
print(f'O menor valor da lista é {min(lista)}')
print(lista)