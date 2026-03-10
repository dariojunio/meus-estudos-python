#criar 3 sets sendo
#lista1 = carro / noite
#lista2 = carro / dia
#lista3 = nao carro

func = set(['Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa'])
dia = set(['Ana', 'Marcos', 'Alice', 'Melissa'])
noite =  set(['Pedro', 'Sophia', 'Bruno'])
tem_carro = set(['Marcos', 'Alice', 'Bruno', 'Melissa'])

lista1 = (noite & tem_carro)
print(lista1)

lista2 = (dia & tem_carro)
print(lista2)

lista3 = (func ^ tem_carro)
print(lista3) 
