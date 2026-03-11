#criar um programa que pede ao usuario 2 numeros e partir deles realizar contas matematicas
def calculos(x, y):
  s = x + y
  sub = x - y
  mul = x * y
  div = x / y
  pot = x ** y

  return (f'Soma: {s}, Subtracao: {sub}, Multiplicacao: {mul}, Divisao: {div}, Potencia: {pot}.')

x = float(input('Digite um numero: '))
y = float(input('Digite um outro numero: '))

calculos(x, y)
