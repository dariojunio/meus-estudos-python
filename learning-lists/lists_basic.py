carros = ['Astra', 'Polo', 'HB20', 'Cruze']
carros[0] = 'BYD Dolphin' #trocando um valor
print(carros[2]) #puxando um valor especifico
carros.sort()
print(carros)
len(carros)

#--------------------------------------------

letras = ['a', 'b']
numeros = [1, 2]
i = letras + numeros #podemos usar letras.append(numeros)
print(i)

#--------------------------------------------

z = [[1, 2, 3],[4, 5, 6]]

print(z[1][2]) #posso puxar um valor dentro de um index --> item
