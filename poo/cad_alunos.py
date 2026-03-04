class Alunos:
  def __init__(self, nome, idade, turno):
    self.nome = nome 
    self.idade = idade
    self.turno = turno

  def mostrar_info(self):
    print(f'O aluno(a) {self.nome}, tem {self.idade} anos e estuda no periodo {self.turno}.')


db_alunos = [] 
def cadastrar_aluno():
  while True:
    print('\n===== CADASTRO DE ALUNOS =====')

    input_nome = input('Qual o nome do aluno(a)?, ou aperte [0] para sair. ')
    if input_nome == '0':
        break
    input_idade = input('Qual o idade do aluno(a)?')
    input_turno = input('Qual o turno do aluno(a)?')

    cad_aluno = Alunos(input_nome, input_idade, input_turno)

    db_alunos.append(cad_aluno)
    print(f'\nAluno(a) {input_nome} adicionado com sucesso!')


def listar_alunos():
  print('Alunos cadastrados:')
  for aluno in db_alunos:
    aluno.mostrar_info()



while True:
  print ('\nAdministrador, seja bem vindo a database da E.E. Madre Teresa!')
  log = int(input ('\nEscolha uma opcao [1] Cadastrar aluno | [2] Listar alunos cadastrados | [0] Sair '))
  if log == 1:
    cadastrar_aluno()
  elif log == 2:
    listar_alunos()
  else:
    print('\nSaindo da aplicacao.. Até breve!')
    break


