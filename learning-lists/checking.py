#verificar itens dentro de uma lista

cores = ['azul', 'branca', 'amarelo', 'rosa', 'verde']
cores.sort()

c = input('Qual cor voce deseja procurar no estoque? ')

if c.lower() in cores:  #.lower para facilitar a busca
  print(f'A cor {c} está disponivel!') 
else:
  print('Cor nao encontrada')
