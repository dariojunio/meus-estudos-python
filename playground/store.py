class Celular:
  def __init__(self, modelo, memoria, condicao):
    self.modelo = modelo
    self.memoria = memoria
    self.condicao = condicao


class Loja:
  def __init__(self):
    self.loja = []


  def menu(self):
    while True:
      print('=====LOJA DE TELEFONES D9=====')
      print ('[1] - Cadastrar telefone')
      print ('[2] - Dar baixa em um telefone')
      print ('[3] - Listar telefones')
      print ('[0] - Sair')
      opcao = int(input('\nEscolha uma opcao: '))

      if opcao == 1:
        self.cadastrar()
      elif opcao == 2:
        self.dar_baixa()
      elif opcao == 3:
        self.listar()
      elif opcao == 0:
        print('Saindo do sistema!..')
        break
      else:
        print('Opcao invalida!')

    
  def cadastrar(self):
    modelo = input('Modelo do telefone: ')
    ram = input('Memoria do telefone: ')
    condicao = input('Condicao do telefone: ')
    novo_cell = Celular(modelo, ram, condicao)
    self.loja.append(novo_cell)
    print(f'O telefone {modelo}, foi adicionado em nossa prateleira')
      

  def dar_baixa(self): 
    vendido = input('Qual o modelo do telefone vendido? ')
    for t in self.loja:
      if t.modelo.lower() == vendido.lower():
        self.loja.remove(t)
        print('Tudo certo! telefone colocado como vendido!')
      else:
        print('Telefone nao encontrado')


  def listar(self):
    print('\n---TELEFONES DISPONIVEIS---')
    for t in self.loja:
      print(f'Modelo: {t.modelo:15} | Memoria:{t.memoria} | Condicao:{t.condicao}')


app = Loja()
app.menu()
