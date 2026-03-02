#D9 PARK

vagas_totais = 10
vagas_ocupadas = 0

def registrar_entrada (vagas_atuais, ocupadas):
  if ocupadas < vagas_atuais:
    print('Um carro registrado!')
    return vagas_ocupadas + 1
  else:
    print('Ultimo carro registrado, a partir de agora é necessario esperar uma vaga ser liberada!')


def registrar_saida (ocupadas):
  if ocupadas > 0:
    print('Um carro deixou o estacionamento')
    return ocupadas - 1
  else:
    print ('Ultimo carrro estacionado saindo agora, a partir desse momento o estacioamento está totalmente vazio!')

while True:
  print ('===== D9 PARK =====')
  print (f'Status Atual: Vagas Livres: {vagas_totais}, Vagas ocupadas: {vagas_ocupadas}')
  print ('--- PAINEL DE CONTROLE D9 PARK ---')
  painel = int(input('[1] Entrada | [2] Saída | [0] Encerrar, Escolha sua opcao: ')) 

  if painel == 1 and vagas_totais >= 1:
    vagas_totais = vagas_totais - 1
    vagas_ocupadas = vagas_ocupadas + 1
    registrar_entrada(vagas_totais, vagas_ocupadas)

  elif painel == 2 and vagas_ocupadas >= 1:
    vagas_totais = vagas_totais + 1
    vagas_ocupadas = vagas_ocupadas - 1
    registrar_saida(vagas_ocupadas)

  else:
    print('Saindo do painel de controle!')
    break 





