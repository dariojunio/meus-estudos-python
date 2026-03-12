#crie uma lista de carros em estoque e peça ao usuario um modelo de carro para compra, retorne uma resposta conforme disponibilidade no estoque
store = ['BMW X6', 'BMW i5', 'BMW i8']

def comprar(pergunta):
    for c in store:
      if c.lower() == pergunta.lower():
        print ('\nEste carro esta disponivel para compra!')
        break
    else:
      print ('\nCarro indisponivel para compra!')
  

def app():
  print('Seja bem vindo(a) a nossa loja BMW! Esses sao nossos modelos disponiveis para compra')
  print('')
  for d in store:
    print (f'Modelo: {d}')
    

app()
pergunta = input('\nQual carro deseja comprar?')
comprar(pergunta)
