class Jogo():
  def __init__(self, versao, nome):
    self.versao = float(versao)
    self.nome = nome

  def informacoes_jogo(self):
    print(f'Jogo: {self.nome}')
    print(f'Versao: {self.versao}')

  def mudar_versao(self,nova_versao):
    if nova_versao <= self.versao:
      print('O jogo já tem essa versao atualizada!')
      return
    self.versao = nova_versao
    print(f'O jogo {self.nome} foi atualizado para a versao {nova_versao}')


jogo1 = Jogo (1.0 ,'League of Legends')

jogo1.informacoes_jogo()

jogo1.mudar_versao(2.0)
jogo1.informacoes_jogo()

jogo1.mudar_versao(1.0)
jogo1.mudar_versao(2.5)
