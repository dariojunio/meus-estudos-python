class Lutadores:
  def __init__(self,nome,dano):

    self.nome = nome
    self.dano = dano
    self.vida = 100

  def exibir_info(self):
    print(f'O lutador {self.nome} tem {self.vida} de vida!')

  def atacar(self,oponente):
    oponente.vida = oponente.vida - self.dano
    print(f'O lutador {self.nome} atacou {oponente.nome} causando {self.dano} de dano!')

    if oponente.vida <= 0:
      oponente.vida = 0
      print (f'K.O.! {oponente.nome} foi derrotado!')

  def esta_vivo(self):
    if self.vida > 0:
     return True
    else:
     return False


lutador1 = Lutadores('Ryu', 25)
lutador2 = Lutadores('Ken', 20)
