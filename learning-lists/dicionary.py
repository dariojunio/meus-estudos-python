#dicionarios

aluno = {'nome':'Daniel', 'idade': 23, 'nota_final': 10}


aluno['nota_final'] = 9 #modificar valores


aluno.update({'nome': 'Pedro', 'idade': 22, 'aprovado': True, 'materias': ['Portugues', 'Matematica', 'Redacao']}) #modificar e/ou cria mais de um valor por vez

for keys, values in aluno.items(): #visualiza os valores sem estar dentro de uma tupla
  print(keys, values)
