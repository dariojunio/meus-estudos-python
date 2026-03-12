numeros = []
for n in range(1,11):
  numeros.append(n) 

#nao preciso criar um loop for | numeros = list(range(1,11))
 
for p_i in numeros:
  cal = p_i % 2  #poderia ter feito direto | if p_i % 2 == 0
  if cal == 0:
    print(f'O numero {p_i} é par')
  else:
    print(f'O numero {p_i} é impar')
