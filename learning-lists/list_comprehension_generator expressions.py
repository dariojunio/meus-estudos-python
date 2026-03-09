#list comprehension - usada para criar uma nova lista em cima de uma lista existente

frutas1 = ['abacate', 'morango', 'kiwi']

frutas2 = [fruta for fruta in frutas1 if 'k' in fruta]
print(frutas2)

print('-----------------------------------------------')

numeros1 = [0, 10, 20, 30 , 40, 50]
numeros_com_10 = [numero + 10 for numero in numeros1] #imprimindo JA DENTRO DE UMA LISTA usando for loop
print(numeros_com_10)

print('-----------------------------------------------')

from sys import getsizeof

gen_exp = (a * 10 for a in range(1000)) #generator expressions - uma forma mais rapida para usar for dentro de listas
print(list(gen_exp))
print(getsizeof(gen_exp))
