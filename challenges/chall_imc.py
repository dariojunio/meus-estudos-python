#calculadora imc

def calcular_imc(altura, peso):

  z = altura * altura
  x = peso / z

  if x < 18.5:
    print(f'Voce tem o IMC de {x:.1f} - Magreza')
  elif x <= 24.9:
    print(f'Voce tem o IMC de {x:.1f} - Normal')
  elif x <= 29.9:
    print(f'Voce tem o IMC de {x:.1f} - Sobrepeso')
  elif x <= 39.9:
    print(f'Voce tem o IMC de {x:.1f} - Obesidade')
  else:
    print(f'Voce tem o IMC de {x:.1f} - Obesidade Grave!')

altura = float(input('Qual sua altura?, separe a altura dos centimetros com um ponto. '))
peso = float(input('Qual o seu peso? '))

calcular_imc (altura, peso)

