class Carro:
  def __init__(self, nome, potencia, ano):
    self.nome = nome
    self.potencia = potencia
    self.ano = ano

class Garagem:
  def __init__(self, dono):
    self.garagem = []
    self.dono = dono

  def adicionar_carros(self, *carro): #* transforma a lista numa tupla
    self.garagem.extend(carro)

  def listar_carros(self):
    for c in self.garagem:
      print(f'Carro: {c.nome}, Potencia de {c.potencia} cavalos, criado em {c.ano}.')
  


garagem1 = Garagem('Junior') #adicionando diretamente de dentro do metodo
garagem1.adicionar_carros(
    Carro('Aston Martin Valkyrie', 1176, 2024),
    Carro('Koenigsegg Jesko Absolut', 1600, 2022),
    Carro('Lamborghini Veneno', 750, 2020)
)

garagem1.listar_carros()


