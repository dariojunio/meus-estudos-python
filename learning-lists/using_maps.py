#map function - com ele é possivel aplicar uma funcao aos itens de uma lista

def i(x):
  return x + 10

lista1 = map(i, [1, 3, 5, 7])
print(list(lista1))
