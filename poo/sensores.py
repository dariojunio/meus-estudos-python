class Sensor:
  def __init__(self, nome, localizacao):

    self.nome = nome
    self.localizacao = localizacao

  def exibir_status(self):
    print(f'O sensor {self.nome} que está localizado em {self.localizacao} está ativo!')


class SensorTemperatura(Sensor):

  def __init__(self, nome, localizacao, valor):
    super().__init__(nome, localizacao)
    self.valor = valor

  def ler_dado(self):
    if not self.valor > 50:
      print(f'Temperatura Atual: {self.valor}°C.')
    else:
      print('ALERTA DE INCÊNDIO! 🔥')


class SensorPresenca(Sensor):

  def __init__(self, nome, localizacao, movimento):
    super().__init__(nome, localizacao)
    self.movimento = movimento

  def ler_dado(self):
    if self.movimento == True:
      print('Movimento Detectado!')
    else:
      print('Área vazia.')


sensores = [
    SensorTemperatura(nome='G1',localizacao='Garagem',valor=60),
    SensorPresenca(nome='C1',localizacao='Cozinha',movimento=True)
    ]

for sts in sensores:
  sts.exibir_status()
  sts.ler_dado()




