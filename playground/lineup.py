class Jogadores():
  def __init__(self, nome, idade, posicao):
    self.nome = nome
    self.idade = idade
    self.posicao = posicao

  def mostrar_info_jogadores(self):
    print(f'O Jogador {self.nome} tem {self.idade} e joga como {self.posicao}')

lineup_lol = []


def cad_jogador_menu():
  while True:
    print('===== CADASTRO DE JOGADORES =====')
    nick_ipt = input('Para começar, digite o nick do jogador ou pressione [0] para sair do menu. ')
    if nick_ipt == '0':
      break
    idade_ipt = input(f'Certo! Agora digite a idade do jogador {nick_ipt}: ')
    posicao_ipt = input(f'Certo! Agora digite a posicao que o jogador {nick_ipt} joga!: ')
    print('Jogador adicionado com sucesso!')

    novo_jogador = Jogadores(nick_ipt, idade_ipt, posicao_ipt)
    lineup_lol.append(novo_jogador)

                                  
def listar_jogadores():
    for j in lineup_lol:
      j.mostrar_info_jogadores()
    


def sacar_jogador():
  while True:
    print('===== REMOVER DE JOGADORES =====')
    remover_input = input('Digite o nick do jogador para remover da lineup ou pressione [0] para voltar. ')
    if remover_input == '0':
      break
    encontrado = False
    for j in lineup_lol:
      if j.nome.lower() == remover_input.lower():
        lineup_lol.remove(j)
        print(f'\n{j.nome} removido da lineup!')
        encontrado = True
        break
    if not encontrado:
        print('Jogador nao cadastrado.')
    


while True:
  print('\n===== PAINEL DE CONTROLE - LINEUP LOL=====')
  log = input('\nSeja bem vindo!, escolha uma opcao: [1] - Cadastrar jogador || [2] - Retirar jogador || [3] - Lista de jogadores || [0] - Sair ')
  if log == '1':
    cad_jogador_menu()
  elif log == '2':
    sacar_jogador()
  elif log == '3':
     listar_jogadores()
  elif log == '0':
    print('Saindo da aplicacao... Até breve!')
    break
  else:
    print('Opcao invalida, tente novamente!')

